'''
@Author: your name
@Date: 2020-02-18 16:09:51
@LastEditTime: 2020-02-27 10:47:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\Trump\数据分析.py
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
                         'Twitter Web Client'])].groupby(['source',data['local_time'].dt.year]).size().reset_index()
print(river_data)
'''
#改名
river_data.rename(columns={0:'number'}, inplace=True)
river_data['local_time'] = river_data['local_time'].astype(str)
river_data = river_data[['local_time', 'number', 'source']]
##把dataframe变成list
river_data = river_data.values.tolist()

# 每天什么时候发推？
by_hour = data[data['local_time'] > pd.to_datetime('2019/1/1 00:00:00')].groupby(data['local_time'].dt.hour).size()
# by_hour = data.groupby(data['local_time'].dt.hour).size()


#2.2 最不受特朗普待见的美国主流媒体是什么？###############################
data['text'].sample(5)
us_media = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\Trump\us_media.csv')
medias = [m.lower() for m in list(us_media['media'])]
#pandas.Series.str.lower
mentioned_count = [data['text'].str.lower().str.contains(media).sum() for media in medias]
us_media['mentioned_count'] = mentioned_count
media_top10 = us_media.sort_values(by='mentioned_count', ascending=False)[:10]


#停用词表
stop_words_en = []
with open('GitHub项目\interesting_python\Trump\stop_words_en.txt', 'r') as f:
    stop_words_en = [i.strip() for i in f.readlines()]
    
stop_words_en = list(set(stop_words_en))
stop_words_en.append('')
#map函数第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
stop_words_en.extend(list(map(str,list(range(10)))))
stop_words_en.extend(['http', 'https', 'amp;', "Don't", 'RT'])
stop_words_en.extend(list('ABCDEFGHIJKLMMOPQRSTUVWXYZ'))
stop_words_en.extend(list('abcdefghijklmnopqrstuvwxyz'))


def get_word_cloud(text_column):
    text = ' '.join(list(text_column))
    r =  "【.*?】+|\\《.*?》+|\\#.*?#+|[.!/_,$&%^*()<>+""'?@|:~{}#]+|[——！，。=？、：“”‘’￥……（）《》【】\"]"
    for i in list(r):
        text = text.replace(i, ' ')
    
    split_text = text.split(' ')
    text_list = [i for i in split_text if i not in stop_words_en]
    
    c = Counter()
    c = Counter(text_list)
    wc_data = pd.DataFrame({'word':list(c.keys()), 'counts':list(c.values())}).sort_values(by='counts', ascending=False).head(70)
    
    wordcloud = WordCloud(width=1000, height=600)
    wordcloud.add("", wc_data['word'], wc_data['counts'], word_size_range=[20, 100])
    return wordcloud 

#contains内置正则表达式，这里就是代表'或'的用法
#print(data.loc[data['text'].str.lower().str.contains('|'.join(medias)), 'text'].shape)
data[(data['text'].str.lower().str.contains('nbc'))&
    data['text'].str.lower().str.contains('fake news')]['id_str'].sample(5)
data[(data['text'].str.lower().str.contains('cnn'))&
    data['text'].str.lower().str.contains('fake news')]['id_str'].sample(5)
#get_word_cloud(data.loc[data['text'].str.lower().str.contains('|'.join(medias)), 'text']).render(r'E:\vscode_code\GitHub项目\interesting_python\Trump\词表.html')
# 一共发了612条推特抨击Fake News！
data['text'].str.lower().str.contains('fake news').sum()



#7. 跟中国有关的推特##############################################
data_china = data[data['text'].str.lower().str.contains('china|chinese')]
'''