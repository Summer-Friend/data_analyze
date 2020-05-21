'''
@Author: your name
@Date: 2020-01-31 11:49:57
@LastEditTime : 2020-02-04 20:10:48
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\数据可视化\数据处理\数据处理.py
'''
import pandas as pd
import numpy as np
from numpy import nan as NaN
import openpyxl

data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\数据可视化\数据处理\directory.csv',encoding='utf-8')
data2_read=pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\数据可视化\数据处理\dictory_test.csv')
#打印前五个
# #print(data.head())
#包括数量，平均值，均方差等
#print(data.describe())
#记录数据为空或为NaN时的个数
#print(data2_read.isnull().sum())
#data2_read = data2_read[data2_read['state'=='Ohio1']]
#print(data2_read.isnull().sum())

#计算数量并取前十名，因为这个CSV文件有缺失，所以只显示出两个
country_count = data['Country'].value_counts()[0:10]
print(country_count)

#print(data2_read[data2_read['year']].notnull())
new_data = data[data['Brand'].notnull()]
print(new_data.head())
print(data['Brand'].notnull().head())