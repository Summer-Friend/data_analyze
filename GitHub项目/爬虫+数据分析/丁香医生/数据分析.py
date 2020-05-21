'''
@Author: your name
@Date: 2020-02-07 11:15:16
@LastEditTime : 2020-02-07 17:57:47
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\爬虫+数据分析\丁香医生\数据分析.py
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import Bar,Map
from pandas.io.json import json_normalize

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  #解决seaborn中文字体显示问题
plt.rc('figure', figsize=(10, 10))  #把plt默认的图片size调大一点
plt.rcParams["figure.dpi"] =mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


all_data = pd.read_csv(r'E:\vscode_code\GitHub项目\爬虫+数据分析\丁香医生\all_data.csv')
#all_data = pd.DataFrame(all_data)
# 1.2 把无用的字段删去
all_data.drop(columns=['_id', 'entLogo', 'region'], inplace=True)
# 1.3 根据id去重
all_data.drop_duplicates(subset='id', inplace=True)
#print(all_data.shape)
# 1.4 创建时间、更新时间 数据类型转换
all_data['createTime'] = pd.to_datetime(all_data['createTime'])
all_data['updateTime'] = pd.to_datetime(all_data['updateTime'])

# 1.5 由于儿科的数据是按照市为单位爬取的，而其它科是按省爬取的，所以area没有参考意义，需要清理出省
all_data['locationText'].unique()
all_data.loc[all_data['depType'] != '儿科', 'province'] = all_data.loc[all_data['depType'] != '儿科', 'area']
all_data.loc[(all_data['locationText'].str.contains('北京|上海|天津|重庆|自治区|省'))&
             (all_data['depType'] == '儿科'), 'province']= all_data.loc[(all_data['locationText'].str.contains('北京|上海|天津|重庆|自治区|省'))&
                                                                      (all_data['depType'] == '儿科'), 'locationText'].str.split('省|自治区|市', expand=True)[0]
all_data['city'] = all_data['locationText'].str.extract(r'(.{2}市)')


'''
#######################################函数语法测试#################################################
#下面这几句话的区别要感受一下
print(all_data['typeText'].head())
print(all_data['typeText'].value_counts())

#带有选择的选取部分数据操作
print(all_data.loc[all_data['depType']=='儿科', 'typeText'].value_counts())
print(all_data[all_data['depType']=='儿科']['typeText'].value_counts())

print(all_data.loc[all_data['depType']=='儿科', 'typeText'].head())
print(all_data[all_data['depType']=='儿科']['typeText'].head())

#这是错误的操作
print(all_data[all_data['depType']=='儿科', 'typeText'].value_counts())
'''

"""
# 1.6 工资字段很乱，需要定义一个函数处理
all_data['salaryText'].unique()
def process_k(data):
    if '千' in data:
        return float(data.replace('千', '')) * 1000
    elif '万' in data:
        return float(data.replace('万', '')) * 10000


def process_salary(data):
    if data == '面议':
        return np.nan
    if '万以上' in data:
        return float(data.replace('万以上', '')) * 10000
    if '千以下' in data:
        return float(data.replace('千以下', '')) * 1000
    if '-' in data:
        low, high = data.split('-')
        return (process_k(low) + process_k(high))/2
all_data['salary'] = all_data['salaryText'].apply(process_salary)
all_data = all_data[-(all_data['salary']>100000)]
#all_data.info()

#print(all_data.iloc[2600])

#直接用.shape可以快速读取矩阵的形状，使用shape[0]读取矩阵第一维度的长度
all_data[all_data['depType']=='儿科'].shape[0]

# 招聘儿科医生的单位类型占比
type_pct = all_data.loc[all_data['depType']=='儿科', 
                        'typeText'].value_counts()/all_data[all_data['depType']=='儿科'].shape[0]*100

bar = Bar("各类型单位招聘儿科岗位数百分比", width = 700,height=500)
bar.add("", type_pct.index, np.round(type_pct.values, 1), is_stack=True, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, is_label_show=True,
       xaxis_rotate=20)
bar.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\丁香医生\各类型单位招聘儿科岗位数百分比.html')

# 公立/民营医院儿科医生招聘经验要求百分比
np.round(all_data.loc[all_data['depType']=='儿科', 
                        'jobYearText'].value_counts()/all_data[all_data['depType']=='儿科'].shape[0]*100, 1)
np.round(all_data.loc[(all_data['depType']=='儿科')&(all_data['typeText']=='公立医院'), 
                      'jobYearText'].value_counts()/all_data[(all_data['depType']=='儿科')&(all_data['typeText']=='公立医院')].shape[0]*100,1)
np.round(all_data.loc[(all_data['depType']=='儿科')&(all_data['typeText']=='民营医院'), 
                      'jobYearText'].value_counts()/all_data[(all_data['depType']=='儿科')&(all_data['typeText']=='民营医院')].shape[0]*100,1)

exp = ['应届生', '1-3年', '3-5年', '5-10年', '10年以上', '经验不限']
exp1 = [1.6, 12.9, 14.4, 14.8, 6.4, 49.4]
exp2 = [2.5, 9.2, 7.7, 8.1, 3.7, 68]
exp3 = [0.5, 17.8, 22.3, 21.1, 9.7, 28.7]
bar = Bar("公立/民营医院儿科医生招聘工作经验要求百分比", width = 600,height=500)
bar.add("平均",exp, exp1, is_stack=False, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, 
        is_label_show=True, legend_top=30, xaxis_rotate=20)
bar.add("公立医院",exp, exp2, is_stack=False, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, 
        is_label_show=True, legend_top=30, xaxis_rotate=20)
bar.add("民营医院",exp, exp3, is_stack=False, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, 
        is_label_show=True, legend_top=30, xaxis_rotate=20)
bar.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\丁香医生\医生招聘工作经验要求百分比.html')


# 公立/民营医院儿科医生招聘职称要求百分比
np.round(all_data.loc[all_data['depType']=='儿科', 
                        'positText'].value_counts()/all_data[all_data['depType']=='儿科'].shape[0]*100, 1)
np.round(all_data.loc[(all_data['depType']=='儿科')&(all_data['typeText']=='公立医院'),'positText'].value_counts()/all_data[(all_data['depType']=='儿科')&(all_data['typeText']=='公立医院')].shape[0]*100,1)
np.round(all_data.loc[(all_data['depType']=='儿科')&(all_data['typeText']=='民营医院'),'positText'].value_counts()/all_data[(all_data['depType']=='儿科')&(all_data['typeText']=='民营医院')].shape[0]*100,1)


level = ['初级', '中级', '副高', '高级', '不限']
level1 = [27.6, 17.2, 10.5, 2.5, 36.4]
level2 = [25, 8.1, 10.7, 3, 46.6]
level3 = [33.2, 26.3, 10.3, 1.9, 23.7]
bar = Bar("公立/民营医院儿科医生招聘职称要求百分比", width = 600,height=500)
bar.add("平均",level, level1, is_stack=False, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, 
        is_label_show=True, legend_top=30, xaxis_rotate=20)
bar.add("公立医院",level, level2, is_stack=False, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, 
        is_label_show=True, legend_top=30, xaxis_rotate=20)
bar.add("民营医院",level, level3, is_stack=False, 
       xaxis_label_textsize=20, yaxis_label_textsize=14, 
        is_label_show=True, legend_top=30, xaxis_rotate=20)
bar.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\丁香医生\医生招聘职称要求百分比.html')


#全国各区域对于儿科医生的需求
# 对于province的处理结果还不是很满意，再处理以下
def get_province(data):
    province = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', 
            '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', 
            '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', 
            '新疆', '台湾', '香港', '澳门', '国外']
    for i in province:
        if i in data:
            return i
        
all_data.loc[all_data['depType']=='儿科', 'province2'] = all_data.loc[all_data['depType']=='儿科', 'locationText'].apply(get_province)
demand = all_data.loc[all_data['depType']=='儿科', 'province2'].value_counts()
province = list(demand.index)
value = list(demand.values)
province.extend(['内蒙古', '山西', '青海'])
value.extend([1,1,1])

map = Map("儿科医生全国各区域需求量", width=600, height=600)
map.add(
    "",
    province,
    value,
    maptype="china",
    is_visualmap=True,
    visual_text_color="#000",
)
map.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\丁香医生\儿科医生全国各区域需求量.html')


# 不同科室招聘持续时间
#两个一样的用法，pd.to_timedelta和两个pd.to_datetime相减都是得到的Timedelta类型，即时间差
all_data['time_delta'] =  pd.to_datetime(all_data['updateTime'])-pd.to_datetime(all_data['createTime'])
#all_data['time_delta'] =  pd.to_timedelta(all_data['updateTime']-all_data['createTime'])
print(all_data.loc[all_data['depType']=='儿科', 'time_delta'].mean())
print(all_data.loc[all_data['depType']=='妇产科', 'time_delta'].mean())
print(all_data.loc[all_data['depType']=='眼科', 'time_delta'].mean())
print(all_data.loc[all_data['depType']=='内科', 'time_delta'].mean())
print(all_data.loc[all_data['depType']=='外科', 'time_delta'].mean())

#儿科的工资待遇
#sort_values()用于排序，可内置参数
mean_salary = all_data.groupby('depType')['salary'].mean().sort_values()

#提供数组
grade_same1 = np.round(np.array([3, 31, 12, 1, 0]) / (3+31+12+1)*100, 1)
print(grade_same1)

#像这样的单步调试可以很好地看到数据的每个条例的对应关系，而不需要去从csv文件里面找
#print(all_data.iloc[888])
"""

