'''
@Author: your name
@Date: 2020-02-01 14:34:30
@LastEditTime : 2020-02-01 18:14:11
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\天气实时\数据分析.py
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts import Line

#基础读取
data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\天气实时\AQI_Data.csv')
#data.info()
#data['time'].unique()

# 数据清洗
#转换时间类型
data['time'] = pd.to_datetime(data['time'])
data = data[data['time']<=pd.to_datetime('2019-02-11 23:59:59')]  # 选取2月4日——2月12日的数据
data.set_index('time',inplace=True)
data = data.replace('—', np.nan)
for col in ['AQI', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']:
    data[col] = data[col].astype(float)
#data.head()
print(data.head())
'''
AQI_total_mean = data[data['time']<=pd.to_datetime('2019-02-06 23:59:59')].groupby(['time'])['AQI'].mean()
line = Line("全国春节期间空气质量指数总体趋势", "2019年除夕到初二", width=800)
line.add("", AQI_total_mean, np.round(AQI_total_mean.values,0), is_smooth=True, 
         legend_text_size=18,xaxis_label_textsize=14,yaxis_label_textsize=18,
         xaxis_rotate=20, yaxis_min=8, mark_point=["max"])
line.render('全国春节期间空气质量指数总体趋势.html')
'''
