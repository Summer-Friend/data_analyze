'''
@Author: your name
@Date: 2020-02-01 14:34:30
@LastEditTime : 2020-02-01 19:01:35
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\天气实时\数据分析.py
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts import Line,Bar


data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\天气实时\data_clean.csv')
#转换时间类型
data['time'] = pd.to_datetime(data['time'])

AQI_total_mean = data[data['time']<=pd.to_datetime('2019-02-06 23:59:59')].groupby(['time'])['AQI'].mean()
#print(AQI_total_mean.index)
#print((np.round(AQI_total_mean.values,0))
#折线图统计
#貌似是数据太多画不出来了
line = Line("全国春节期间空气质量指数总体趋势", "2019年除夕到初二", width=800)
line.add("", AQI_total_mean.index, np.round(AQI_total_mean.values,0), is_smooth=True, 
         legend_text_size=18,xaxis_label_textsize=14,yaxis_label_textsize=18,
         xaxis_rotate=20, yaxis_min=8, mark_point=["max"])
line.render('全国春节期间空气质量指数总体趋势.html')


#柱状图统计
#1.
data2 = data[data['time']<=pd.to_datetime('2019-02-05 23:59:59')]
data_AQI_min = data2.groupby('city')['AQI'].min()
data_AQI_max = data2.groupby('city')['AQI'].max()
data_AQI_times = np.round(data_AQI_max/data_AQI_min, 1)
#找到data_AQI_times中最大的10个类别，与之对应的是nsmallest
data_AQI_times_top10 = data_AQI_times.nlargest(10)
bar = Bar("全国除夕和春节期间空气质量最高最低比Top10城市", "时间：2019年除夕至初一", width=600)
#index和values只是为了确定索引值和狄莺的值用于横纵坐标画图
bar.add("", data_AQI_times_top10.index, data_AQI_times_top10.values, is_stack=True, 
        is_label_show=True,bar_category_gap='40%', label_color = ['#130f40'], label_text_size=18,
       legend_text_size=18,xaxis_label_textsize=14,yaxis_label_textsize=18, xaxis_rotate=30)
bar.render("全国除夕和春节期间空气质量最高最低比Top10城市.html")

#2.
data_AQI_times_counts = data_AQI_times.value_counts(bins=[1,5,10,15,20,25])
bar = Bar("全国除夕和春节期间空气质量最高最低比的城市数量", "时间：2019年除夕至初一", width=600)
times = ['1-5倍','5-10倍','10-15倍','15-20倍','20-25倍']
bar.add("", times, data_AQI_times_counts.values, is_stack=True, 
        is_label_show=True,bar_category_gap='40%', label_color = ['#130f40'], label_text_size=18,
       legend_text_size=18,xaxis_label_textsize=18,yaxis_label_textsize=18)
bar.render("全国除夕和春节期间空气质量最高最低比的城市数量.html")
print(data_AQI_times_counts)
#下面是value_counts内的参数定义
'''
    4.1 normalize ：计数项归一化；就是得到的结果为频率

    4.2 sort：是否对频率项进行排序，默认降序；

    4.3 ascending ： 排序是否升续排列，默认False；

    4.4 bins： 离散数据的分段，只能作用在数值变量，pd.cut 的简化版；

    4.5 dropna： 不包括对NA的计数；
'''
