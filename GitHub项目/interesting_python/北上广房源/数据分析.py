'''
@Author: your name
@Date: 2020-02-04 20:33:33
@LastEditTime : 2020-02-14 09:54:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\北上广房源\数据分析.py
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import Bar,Line,WordCloud
from scipy import stats
from collections import Counter
from pymongo import MongoClient
from pandas.io.json import json_normalize

data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\data_sample.csv')
# 数据清洗(按列清理)
# 1. 去掉“_id”列
data = data.drop(columns='_id')
#data.drop([1])   #这个就是代表去掉第一行
# 2. bathroom_num
#print(data['bathroom_num'].unique())
#直接根据条件进行索引，isin()接受一个列表，判断该列中元素是否在列表中
data[data['bathroom_num'].isin(['8','9','11'])]
# 3. bedroom_num
data['bedroom_num'].unique()
# 没有异常数据，只是很多10室以上都是专门用来合租的
data[data['bedroom_num'].isin(['10','11','12','13','14','15','20'])]
# 房间只有1平米，是异常数据，删去
#print(data['rent_area'].head())
# rent_area字段有些填写的是一个范围，比如23-25平房米，后期转换成“float”类型的时候不好转换，考虑取平均值
def get_aver(data):
    #isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
    if isinstance(data, str) and '-' in data:
        low, high = data.split('-')
        return (int(low)+int(high))/2
    else:
        return int(data)

data['rent_area'] = data['rent_area'].apply(get_aver)
data = data.drop(data[data['rent_area'] < 5].index)
# 租金都是以“元/月”计算的，所以这一列没用了，可以删了
data = data.drop(columns='rent_price_unit')

# 8. rent_price_listing
#isin(), str.contains()都是pandas用于筛选的函数
data[data['rent_price_listing'].str.contains('-')].sample(3)
# 价格是有区间的，需要按照处理rent_area一样的方法处理
data['rent_price_listing'] = data['rent_price_listing'].apply(get_aver)
# 数据类型转换
for col in ['bathroom_num', 'bedroom_num', 'hall_num', 'rent_price_listing']:
    data[col] = data[col].astype(int)
    
# 'distance', 'latitude', 'longitude'因为有None，需另外处理
def dw_None_dis(data):
    if data is None:
        return np.nan
    else:
        return int(data)
    
#这个玩意儿很重要，因为dropna对缺失值才有效果，对空值是没用的
def dw_None_latlon(data):
    if data is None or data == '':
        return np.nan
    else:
        return float(data)            

data['distance'] = data['distance'].apply(dw_None_latlon)
data['latitude'] = data['latitude'].apply(dw_None_latlon)
data['longitude'] = data['longitude'].apply(dw_None_latlon)

#print(data.sample(5))
data.to_csv(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\data_clean.csv', index=False)


#各城市的租房分布
def get_city_zf_loc(city, city_short, col=['longitude', 'latitude', 'dist'], data=data):
    file_name = 'data_' + city_short + '_latlon.csv'
    data_latlon = data.loc[data['city']==city, col].dropna(subset=['latitude', 'longitude'])
    data_latlon['longitude'] = data_latlon['longitude'].astype(str)
    data_latlon['latitude'] = data_latlon['latitude'].astype(str)
    #参考https://zhuanlan.zhihu.com/p/31974169
    data_latlon['latlon'] = data_latlon['longitude'].str.cat(data_latlon['latitude'], sep=',')
    #data_latlon.to_csv(file_name, index=False)
    #print(city+'的数据一共有{}条'.format(data_latlon.shape[0]))
    
get_city_zf_loc('北京', 'bj', ['longitude','latitude', 'dist'])
get_city_zf_loc('上海', 'sh', ['longitude','latitude', 'dist'])
get_city_zf_loc('广州', 'gz', ['longitude','latitude', 'dist'])
get_city_zf_loc('深圳', 'sz', ['longitude','latitude', 'dist'])


'''
#北上广深依次操作即可
fig = plt.figure(dpi=300)
#滤除缺失数据。如果是Series,则返回一个仅含非空数据和索引值的Series，默认丢弃含有缺失值的行。
#mydf.dropna(subset=[ 列名 ],inplace=True)subset参数指定列,inplace参数为修改原dataframe,
data.dropna(subset=['latitude', 'longitude'])[data['city']=='北京']['dist'].value_counts(ascending=True).plot.barh()
#关于绘图无法显示中文的问题
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#在后续学习seaborn包绘图时，如果绘图之前指定绘图风格，导致不能显示中文时，此时也许会改变原matplotlibrc的配置，尝试增加一句：
#sns.set_style('darkgrid',{'font.sans-serif':'Microsoft YaHei'})
plt.show()

fig = plt.figure(dpi=300)
data.dropna(subset=['latitude', 'longitude'])[data['city']=='上海']['dist'].value_counts(ascending=True).plot.barh()
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.tick_params(axis='both', labelsize = 5)#调整标签大小
plt.show()
'''

#城市各区域的房价分布
data['aver_price'] = np.round(data['rent_price_listing'] / data['rent_area'], 1)
"""
g = sns.FacetGrid(data, row="city", height=4, aspect=2)
#核密度估计(kernel density estimation)是在概率论中用来估计未知的密度函数，属于非参数检验方法之一
#displot()集合了matplotlib的hist()与核函数估计kdeplot的功能，增加了rugplot分布观测条
g = g.map(sns.kdeplot, "aver_price")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.show()
"""



# 由于平均租金基本上都集中在250元/平米/月以内，所以选取这部分数据绘制热力图
def get_city_zf_aver_price(city, city_short, col=['longitude', 'latitude', 'aver_price'], data=data):
    #file_name = 'data_' + city_short + '_aver_price.csv'
    data_latlon = data.loc[(data['city']==city)&(data['aver_price']<=250), col].dropna(subset=['latitude', 'longitude'])
    data_latlon['longitude'] = data_latlon['longitude'].astype(str)
    data_latlon['latitude'] = data_latlon['latitude'].astype(str)
    data_latlon['latlon'] = data_latlon['longitude'].str.cat(data_latlon['latitude'], sep=',')
    #data_latlon.to_csv(file_name, index=False)
    #print(city+'的数据一共有{}条'.format(data_latlon.shape[0]))
    
get_city_zf_aver_price('北京', 'bj')
get_city_zf_aver_price('上海', 'sh')
get_city_zf_aver_price('广州', 'gz')
get_city_zf_aver_price('深圳', 'sz')



# 各城市租金Top10的商圈
#二层分类，先城市分类，再商圈分类，再从['aver_price']挑选前50,再把city
bc_top10 = data.groupby(['city', 'bizcircle_name'])['aver_price'].mean().nlargest(50).reset_index()['city'].value_counts()
bar = Bar("每平米平均租金前50的北上广深商圈数量", width=400)
bar.add("", bc_top10.index, bc_top10.values, is_stack=True,
       xaxis_label_textsize=16, yaxis_label_textsize=16, is_label_show=True)
bar.render(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\每平米平均租金前50的北上广深商圈数量.html')

def get_top10_bc(city, data=data):
    top10_bc = data[(data['city']==city)&(data['bizcircle_name']!='')].groupby('bizcircle_name')['aver_price'].mean().nlargest(10)
    bar = Bar(city+"市每平米平均租金Top10的商圈", width=600)
    bar.add("", top10_bc.index, np.round(top10_bc.values, 0), is_stack=True,
       xaxis_label_textsize=16, yaxis_label_textsize=16, xaxis_rotate=30, is_label_show=True)
    #这句话出错了
    #bar.render(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\city+"市每平米平均租金Top10的商圈".html')
    return bar



# 北京每平米平均租金Top10的商圈
get_top10_bj = get_top10_bc('北京')
get_top10_bj.render(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\北京市每平米平均租金Top10的商圈.html')

#北上广深依次操作
get_top10_gz = get_top10_bc('广州')
get_top10_gz.render(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\广州市每平米平均租金Top10的商圈.html')

#get_top10_bc('上海')
#get_top10_bc('深圳')



#距离地铁口远近有什么关系
def distance_price_relation(city, data=data):
    #双变量图
    #dropna用于删除含有空数据的全部行，可以通过axis参数来删除含有空数据的全部列，
    #可以通过subset参数来删除在指定字典列中含有空数据的全部行
    g = sns.jointplot(x="distance", 
                  y="aver_price", 
                  data=data[(data['city']==city)&
                            (data['aver_price']<=350)].dropna(subset=['distance']), 
                  kind="reg",
                 stat_func=stats.pearsonr)
    g.fig.set_dpi(100)
    g.ax_joint.set_xlabel('最近地铁距离', fontweight='bold')
    g.ax_joint.set_ylabel('每平米租金', fontweight='bold')
    return g
"""
#北上广深依次操作
distance_price_relation_bj = distance_price_relation('北京')
plt.show()
"""


#pd.cut()的作用，有点类似给成绩设定优良中差，比如：0-59分为差，60-70分为中，71-80分为优秀等等,通过bins划分区间
bins = [100*i for i in range(13)]
data['bin'] = pd.cut(data.dropna(subset=['distance'])['distance'], bins)
bin_bj = data[data['city']=='北京'].groupby('bin')['aver_price'].mean()
bin_sh = data[data['city']=='上海'].groupby('bin')['aver_price'].mean()
bin_gz = data[data['city']=='广州'].groupby('bin')['aver_price'].mean()
bin_sz = data[data['city']=='深圳'].groupby('bin')['aver_price'].mean()

#print(bin_bj.index)
#print(bin_bj.values)
"""
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

line = Line("距离地铁远近跟每平米租金均价的关系")
line.add("", a, bin_bj.values,
            legend_text_size=18,xaxis_label_textsize=14,yaxis_label_textsize=18,xaxis_rotate=20, yaxis_min=8, legend_top=30)
             
line.render(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\北京距离地铁远近跟每平米租金均价的关系.html')

#把a换成bin_bj.index不知道为什么就错了
line = Line("距离地铁远近跟每平米租金均价的关系")
for city, bin_data in {'北京':bin_bj, '上海':bin_sh, '广州':bin_gz, '深圳':bin_sz}.items():
    #print(city)
    line.add(city, a, bin_data.values,
            legend_text_size=18,xaxis_label_textsize=14,yaxis_label_textsize=18,
            xaxis_rotate=20, yaxis_min=8, legend_top=30)
line.render(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\距离地铁远近跟每平米租金均价的关系.html')

"""
#点云数据
#北上广深租房时都看重什么
bj_tag = []
for st in data[data['city']=='北京'].dropna(subset=['house_tag'])['house_tag']:
    #split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
    #house_tag标签里面有对房间的具体要求，包含很多空格，于是将它们分别提取出来
    bj_tag.extend(st.split(' '))
#调试数据
#print(data[data['city']=='北京'].dropna(subset=['house_tag'])['house_tag'].sample(100))

#统计字符串中的字符数量用Counter函数
name, value = WordCloud.cast(Counter(bj_tag))
print(WordCloud.cast(Counter(bj_tag)))
#print(Counter(bj_tag))
#print(name,'|',value)
'''
wordcloud = WordCloud(width=500, height=500)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.render(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\标签.html')
'''


