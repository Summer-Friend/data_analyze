'''
@Author: your name
@Date: 2020-02-01 13:31:31
@LastEditTime : 2020-02-01 18:14:29
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\天气实时\函数测试.py
'''
import time
import requests
import pandas as pd
import numpy as np
from lxml import etree
import matplotlib.pyplot as plt
from pyecharts import Line

'''
#这个网站登录貌似不需要headers
res = requests.get('http://datacenter.mee.gov.cn/aqiweb2/')
parsed_text = etree.HTML(res.text)
#这个[0]使得你原本爬取的数据附带的中括号被消去了，原本看着挺不美观的
timestamp = parsed_text.xpath('/html/body/div[3]/p/i/text()')[0].replace('年','-').replace('月', '-').replace('日', ' ').replace('时', ':00:00')
#print(timestamp)

# 直接使用pandas获取和解析数据,pd.read_html：返回 list of dataframes
#endoing则用于解码,res.apparent_encoding用于获取当前编码

#读取格式
pandas.read_html(io, match='.+', flavor=None, header=None, index_col=None,
skiprows=None, attrs=None, parse_dates=False, tupleize_cols=None, thousands=',
', encoding=None, decimal='.', converters=None, na_values=None, keep_default_na=True)[source]

data_res = pd.read_html('http://datacenter.mee.gov.cn/aqiweb2/', encoding = res.apparent_encoding)
print(data_res.head())

#这个[0]代表爬取的是网页上第一个表格
#data = data_res[0]
#data = data_res[1]
header = ['city', 'AQI', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'main_pollution']
data.columns = header
data['time'] = timestamp
#print(res.apparent_encoding)
#print(data.head(10))

data_test = data.head(100)
data_test.to_csv(r'E:\vscode_code\GitHub项目\interesting_python\天气实时\函数测试.csv',index=False, mode='a', header=True)
print("录入成功")
'''
data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\天气实时\函数测试.csv')
data['time'] = pd.to_datetime(data['time'])
#print(data.head())

#DataFrame可以通过set_index方法，可以设置单索引和复合索引。通过索引访问数据 
print(data.set_index(data["time"], inplace=True))

#这里用numpy库中的nan替换掉了'-'，不然报错：ValueError: could not convert string to float: '—'
data = data.replace('—', np.nan)
for col in ['AQI', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']:
#astype实现变量类型转换：astype(type): returns a copy of the array converted to the specified type.
    data[col] = data[col].astype(float)
#print(data.head())
data.to_csv(r'E:\vscode_code\GitHub项目\interesting_python\天气实时\data_clean.csv', index=True)
print(data.head())
print('录入完成')
'''
AQI_total_mean = data[data['time']<=pd.to_datetime('2019-02-06 23:59:59')].groupby(['time'])['AQI'].mean()
print(AQI_total_mean)
line = Line("全国春节期间空气质量指数总体趋势", "2019年除夕到初二", width=800)
line.add("", AQI_total_mean.index, np.round(AQI_total_mean.values,0), is_smooth=True, 
         legend_text_size=18,xaxis_label_textsize=14,yaxis_label_textsize=18,
         xaxis_rotate=20, yaxis_min=8, mark_point=["max"])
line.render('全国春节期间空气质量指数总体趋势.html')
#plt.show()
'''
