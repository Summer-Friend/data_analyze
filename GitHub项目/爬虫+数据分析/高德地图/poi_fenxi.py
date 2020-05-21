'''
@Author: your name
@Date: 2020-02-02 12:04:21
@LastEditTime : 2020-02-02 15:05:43
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\爬虫+数据分析\高德地图\poi_fenxi.py
'''
import numpy as np
import pandas as pd
from pyecharts import Bar,Pie
import folium
from folium import plugins

data = pd.read_csv(r'E:\vscode_code\GitHub项目\爬虫+数据分析\高德地图\poi.csv',encoding='utf-8')
#print(data['typ1'].unique())
#这些个操作貌似还能自动排序
#下面是value_counts内的参数定义
'''
    4.1 normalize ：计数项归一化；就是得到的结果为频率

    4.2 sort：是否对频率项进行排序，默认降序；

    4.3 ascending ： 排序是否升续排列，默认False；

    4.4 bins： 离散数据的分段，只能作用在数值变量，pd.cut 的简化版；

    4.5 dropna： 不包括对NA的计数；
'''

#print(data.groupby('typ1')['typ1'].count())
typ1 = data['typ1'].value_counts()
typ2 = data['typ2'].value_counts()
#print(typ2)
#print(list(typ2.index)[:10])


#绘图
#饼图
attr = list(typ1.index)
v1 = list(typ1)
pie = Pie("服务数量统计", 'center')
pie.add(
    "",
    attr,
    v1,
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
pie.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\高德地图\服务数量统计.html')

#柱状图
attr = list(typ2.index)[:10]
v1 = list(typ2)[:10]
bar = Bar("")
bar.add("", attr, v1,xaxis_interval=0,xaxis_rotate=20,xaxis_margin=8,is_label_show=True)
bar.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\高德地图\中外餐厅类型数量.html')

#地图
m = folium.Map(location=[28.12, 112.59])
m.save(r'E:\vscode_code\GitHub项目\爬虫+数据分析\高德地图\餐厅位置.html')

#热力图
df1 = data[data['typ1'] == '餐饮服务']
print(df1.head())
df2 = data[data['lat']]
print(df2)
'''
df3 = data[data['lon']]
heatmap1 = folium.Map(location=[28.12, 112.59], zoom_start=11)
heatmap1.add_child(plugins.HeatMap([[row["lat"],row["lon"]] for name, row in df1.iterrows()]))
#heatmap1.add_child(plugins.HeatMap(df2,df3))
heatmap1.save(r'E:\vscode_code\GitHub项目\爬虫+数据分析\高德地图\餐厅热力图2.html')
'''