'''
@Author: your name
@Date: 2020-04-01 10:24:05
@LastEditTime: 2020-04-01 11:00:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\数据分析第二版\日期和时间数据类型及工具\test.py
'''
import pandas as pd 
import numpy as np 
from datetime import datetime
import time
from dateutil.parser import parse


#value = '2011-01-03'
#value2 = datetime.strptime(value, '%Y-%m-%d')

value = '2011年1月3号'
value2 = datetime.strptime(value, '%Y年%m月%d号')
print(value2)
#print(parse(value))

#处理成组的日期
datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
a = pd.to_datetime(datestrs)
print(a.year)

x = ['2011年7月6号', '2011年7月9号']
y = pd.to_datetime(x, format = '%Y年%m月%d号')
print(y)
'''
data = {
    'state':['Ohio2','Ohio2','Ohio2','Nevada2','Nevada2'],
    'year':['2002/1/2','2012/3/4','2022/5/6','2012/7/8','2022/9/10'],
    'pop':[1.52,1.72,3.62,2.42,2.92],
    'salary':['5000K/MTH - 20000K/MTH', '12K/MTH - 19K/MTH',
       '4000K/MTH - 6000K/MTH', '14000K/MTH - 22000K/MTH','8000K/MTH - 20000K/MTH'],
    'create_time':[1462451334, 1462451335, 1461231336, 1462451337, 1462451338]
}
data = pd.DataFrame(data)
data['a'] = pd.to_datetime(data.year, format = '%Y/%m/%d')
data['b'] = pd.to_datetime(data.year, format = '%Y-%m-%d')

print(pd.concat([data['a'], data['b']], axis = 1))
print(data['a'])
print(data['b'])
#提取出年月日
#print(data.a.dt.year)
#print(data.a.dt.year, data.a.dt.month, data.a.dt.day)
'''