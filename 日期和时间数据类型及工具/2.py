'''
@Author: your name
@Date: 2020-03-17 09:09:25
@LastEditTime: 2020-03-17 09:29:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\数据分析第二版\日期和时间数据类型及工具\2.py
'''
import pandas as pd 
import numpy as np 
from datetime import datetime
import time 

data = {
    'state':['Ohio2','Ohio2','Ohio2','Nevada2','Nevada2'],
    'year':['2002/1/2','2012/3/4','2022/5/6','2012/7/8','2022/9/10'],
    'pop':[1.52,1.72,3.62,2.42,2.92],
    'salary':['5000K/MTH - 20000K/MTH', '12K/MTH - 19K/MTH',
       '4000K/MTH - 6000K/MTH', '14000K/MTH - 22000K/MTH','8000K/MTH - 20000K/MTH'],
    'create_time':[1462451334, 1462451335, 1461231336, 1462451337, 1462451338]
}
data = pd.DataFrame(data)
data['a'] = pd.to_datetime(data.year, format = '%Y-%m-%d')
#print(data)
#提取出年月日
#print(data.a.dt.year, data.a.dt.month, data.a.dt.day)

#python中type,dtype,astype的作用与使用要注意，第一个针对单个，第二个针对数组等多个元素
print(type(data.a.dt.year))
print(data.a.dt.year.dtype)


#时间戳转换
timestamp = 1462451334

#转换成localtime
time_local = time.localtime(timestamp)
#转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
print (dt)

#pandas里面时间戳转换
data['date']= pd.to_datetime(data['create_time'].values, utc=True, unit='s').tz_convert(
            "Asia/Shanghai").to_period("D")
print(data)

