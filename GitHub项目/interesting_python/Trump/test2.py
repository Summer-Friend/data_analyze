'''
@Author: your name
@Date: 2020-02-27 10:48:46
@LastEditTime: 2020-02-27 10:49:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\Trump\test2.py
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import WordCloud
from collections import Counter



data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\Trump\donald_trump_twitter.csv'
                   , lineterminator="\n")


#1. 数据清洗
#1.1 时间数据清洗###########################
#strftime()——time结构格式化为字符串
#strptime()——字符串格式化为time结构
#使用datetime属性 dt来访问datetime组件：
data['local_time'] = pd.to_datetime(data['created_at']).dt.tz_convert('US/Eastern').dt.strftime('%Y/%m/%d %H:%M:%S')
data['local_time'] = pd.to_datetime(data['local_time'])
#print(data['local_time'].dt.year.head())


#2.1 特朗普使用推特基本情况###############################
#pandas 的 pandas.Series.dt 可以获得日期/时间类型的相关信息
by_year = data.groupby(data['local_time'].dt.year).size()
#print(by_year)
data[data['local_time'] > pd.to_datetime('2019-01-01 00:00:00')].shape[0]
data[data['source']=='Twitter for Android'].groupby(data['local_time'].dt.year).size()
data[(data['local_time'] > pd.to_datetime('2017-01-01'))&
    (data['source'] == 'Twitter for Android')].groupby(data['local_time'].dt.month).size()
data[data['local_time'] > pd.to_datetime('2017-04-01')]['source'].value_counts()

#https://blog.csdn.net/jingyi130705008/article/details/78162758?utm_source=distribute.pc_relevant.none-task
#reset_index可以还原索引，重新变为默认的整型索引,不然得到的就是分类后的数据 
river_data = data[data['source'].isin(['Twitter for iPhone',
                         'Twitter for Android',
                         'Twitter Web Client'])].groupby(['source',data['local_time'].dt.year]).size()
print(river_data)