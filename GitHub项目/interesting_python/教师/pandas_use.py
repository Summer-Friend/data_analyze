'''
@Author: your name
@Date: 2020-01-30 17:04:04
@LastEditTime : 2020-02-01 19:03:02
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\测试\pandas_use.py
'''
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}

data2 = {
    'state':['Ohio2','Ohio2','Ohio2','Nevada2','Nevada2'],
    'year':[2002,2012,2022,2012,2022],
    'pop':[1.52,1.72,3.62,2.42,2.92],
    'salary':['5000K/MTH - 20000K/MTH', '12K/MTH - 19K/MTH',
       '4000K/MTH - 6000K/MTH', '14000K/MTH - 22000K/MTH','8000K/MTH - 20000K/MTH']
}
frame = pd.DataFrame(data)
frame2 = pd.DataFrame(data2)

#print(frame)
frame.to_csv('E:\\vscode_code\\vscode_python_test\\测试\\pandas_use.csv')
frame2.to_csv('E:\\vscode_code\\vscode_python_test\\测试\\pandas_use_2.csv')

frame_read=pd.read_csv('E:\\vscode_code\\vscode_python_test\\测试\\pandas_use.csv')
frame_read2=pd.read_csv('E:\\vscode_code\\vscode_python_test\\测试\\pandas_use_2.csv')
#print(frame_read)
#print(frame_read.info())
#打印state标签下的内容
#print(frame_read['state'].unique())
'''
#分组
frame_read.info()
print(frame_read.sample(2))
'''
frame_read['type']='幼儿园'
frame_read2['type']='中小学'
#合并
frame_wx = pd.concat([frame_read,frame_read2])
#print(frame_wx.head())
#frame_wx.info()
#frame_wx.to_csv('E:\\vscode_code\\vscode_python_test\\测试\\pandas_us_wx.csv')
#print(frame_wx['state'].sample(4))
#输出列
#print(frame_wx['state'].str.split("-", expand=True))
#print(frame_wx['state'].unique())
#利用map对信息进行分析
#exp_map={'Ohio1':'1-2', 'Ohio2':'2-3', 'Nevada3':'4-5', 'Nevada2':'5-6'}
#print(frame_wx['state'].map(exp_map))

def get_salary_jlc(data):
    pat_jlc = r"(.*)K/MTH - (.*)K/MTH"
    if '00' in data:
        low, high = re.findall(pattern=pat_jlc, string=data)[0]
        return (float(low)+float(high))/2/1000
    else:
        low, high = re.findall(pattern=pat_jlc, string=data)[0]
        return (float(low)+float(high))/2
    
frame_wx['salary_clean'] = frame_wx['salary'].apply(get_salary_jlc)
frame_wx.to_csv('E:\\vscode_code\\vscode_python_test\\测试\\pandas_us_wx.csv')
data_jlc=pd.read_csv('E:\\vscode_code\\vscode_python_test\\测试\\pandas_us_wx2.csv')
#print(data_jlc.head())
#针对于DataFrame的apply方法首先就是要对数据进行DataFrame处理，第29,30行;但是，从CSV内读取pandas库会自动转换格式无需再处理
#print(frame_wx['salary'].apply(get_salary_jlc))

#可视化显示
#frame_wx.drop(frame_wx[frame_wx['salary_clean']>10].index, inplace=True)
#这里标签只能用英文，用中文不知道为啥文字出不来
frame_wx['teacher_type'] = 'Chinese'
data_jlc['teacher_type'] = 'English'
data_salary = pd.concat([frame_wx[['salary_clean', 'teacher_type']],
                        data_jlc[['salary_clean', 'teacher_type']]])
#drop方法可以对Series对象删除某项索引值，这里把工资大于14的清洗出来了
#print(frame_wx)
#print(frame_wx[frame_wx['salary_clean']>14])
#但是这个地方因为用了concat，所以导致索引值出现重复，用drop可能出错
#print(frame_wx.drop(frame_wx[frame_wx['salary_clean']>14].index, inplace=True))
#print(frame_wx)

#下面这三列当初是调试的数据
#print(frame_wx)
#print(data_jlc)
#print(data_salary)
'''
#1.用dataframe将原本从CSV提取的数据格式化后可以进行图表的画
pd.DataFrame(data_salary)
g = sns.FacetGrid(data_salary, row='teacher_type', size=4, aspect=2, xlim=(0,20))
g.map(sns.distplot, "salary_clean")

#2.利用rename函数进行格式化
data_salary.rename(columns={'salary_clean':'salary_clean', 'teacher_type':'teacher_type'}, inplace=True)
# sns.set(font_scale=1.5)
#facegrid是为了生成多个图
g = sns.FacetGrid(data_salary, row="teacher_type", size=4, aspect=2, xlim=(0,20))
g.map(sns.distplot, "salary_clean", rug=False)
#函数操过之后一定要用show方法不然出不来图

plt.show()
'''
#print(np.round(frame_wx['salary_clean'].mean(), 2))

#先用groupby对state分类后对salary求平均再对不同组的平均值求平均值
#print(frame_wx.groupby('state')['salary_clean'].mean().mean())
#print(frame_wx.groupby('state')['salary_clean'].describe())

#对数据进行排序，用到了sort_values，by参数可以指定根据哪一列数据进行排序。ascending是设置升序和降序。
#df.sort_values(by='x',assending=False)
#np.round设置保留几位小数
#print(np.round(frame_wx.groupby('state')['salary_clean'].mean().sort_values()[:10], 1))
#找到teacher_type中最大的五个类别，与之对应的是nsmallest
data_type_salary = data_salary['teacher_type'].value_counts().nlargest(5)
print(data_type_salary)
