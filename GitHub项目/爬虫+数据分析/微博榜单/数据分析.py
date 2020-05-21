'''
@Author: your name
@Date: 2020-02-20 18:47:16
@LastEditTime: 2020-02-20 19:23:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\爬虫+数据分析\微博榜单\数据分析.py
'''
import numpy as np
import pandas as pd
from pyecharts import WordCloud

df = pd.read_csv(r'E:\vscode_code\GitHub项目\爬虫+数据分析\微博榜单\weibo.csv',encoding='utf-8')

user = df['user'].value_counts()

wordcloud = WordCloud(width=800, height=620)
wordcloud.add("", list(user.index), list(user.values), word_size_range=[20, 80])
wordcloud.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\微博榜单\user.html')


df['province'] = df['location'].str.split(' ').str[0]
province_top10 = df['province'].value_counts()[:10]

gender = df['gender'].value_counts()

#好像是筛选掉重复的
data4 = df.drop_duplicates('user')
data4 = data4.sort_values(by='followers',ascending=False)[:10]

#榜单分析
df['hour'] = df['created_time'].str.split(':').str[0].str.split(' ').str[-1]
hour = df['hour'].value_counts()
hour = hour.sort_index()

str_data = ''
for i in range(df.shape[0]):
    str_data = str_data + str(df.iloc[i,4])


