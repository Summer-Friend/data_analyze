'''
@Author: your name
@Date: 2020-02-16 14:31:28
@LastEditTime: 2020-03-17 09:12:50
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\日期和时间数据类型及工具\1.py
'''
import pandas as pd 
import numpy as np 
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
import pytz
import time


#字符串和datetime的互相转换
stamp = datetime(2011, 1, 3)
#print(stamp)
str(stamp)

#解析日期
#datetime.strptime可以用这些格式化编码将字符串转换为日期：
#datetime.strptime是通过已知格式进行日期解析的最佳方式，只能处理单个数据
value = '2011-01-03'
value2 = datetime.strptime(value, '%Y-%m-%d')
datestrs = ['7/6/2011', '8/6/2011']
#中括号得加
value3 = [datetime.strptime(x, '%m/%d/%Y') for x in datestrs]
#print(value3)

#dateutil可以解析几乎所有人类能够理解的日期表示形式：
(parse('2011-01-03'))
(parse('Jan 31, 1997 10:45 PM'))
#在国际通用的格式中，日出现在月的前面很普遍，传入dayfirst=True
parse('6/12/2011', dayfirst=True)

#处理成组的日期
datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
pd.to_datetime(datestrs)

#处理缺失值，配合pandas
idx = pd.to_datetime(datestrs + [None])
pd.isnull(idx)


#时间序列基础##############################################
#1.根据标签索引选取数据时，时间序列和其它的pandas.Series很像
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = pd.Series(np.random.randn(6), index=dates)
#下面几种用法一样
ts[ts.index[4]]
ts['1/10/2011']
ts['20110110']
ts['2011-1-2']
ts[datetime(2011,1,2)]

#对于较长的时间序列，只需传入“年”或“年月”即可轻松选取数据的切片：
#数字个数和日期个数必须对应
longer_ts = pd.Series(np.random.randn(10),
                       index=pd.date_range('1/1/2000', periods=10))
#用法多样，只要索引符合规范
ts['2011-1-2':]
ts[datetime(2011, 1, 7):]
ts['1/6/2011':'1/11/2011']

#2.面这些操作对DataFrame也有效
#生成的就是一个DatetimeIndex
#pd.date_range(start='2012-04-01 12:56:31', periods=20, normalize=True) 
# 可以用start或end指定,normalize选项规范化（normalize）到午夜的时间戳
dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100, 4),
                       index=dates,
                       columns=['Colorado', 'Texas',
                                    'New York', 'Ohio'])
long_df.loc['5-2001']

#产生重复
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000',
                           '1/2/2000', '1/3/2000'])
print(dates.dt.tz_convert('America/New_York'))

dup_ts = pd.Series(np.arange(5), index=dates)

#is_unique可以检查名字是否唯一
dup_ts.index.is_unique

#传入level=0：可以把重复的索引分开
grouped = dup_ts.groupby(level = 0)
grouped.mean()
grouped.count()

#时区划分
#时区名字
#时区是以UTC偏移量的形式表示的
pytz.common_timezones[1:15]
#获取时区对象
tz = pytz.timezone('America/New_York')

#freq就表示时间频率，D代表day，W就代表week，tz就代表时区
rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
#rng2已经规定了时区，相当于已经本地化过了
rng2 = pd.date_range('3/9/2012 9:30', periods=6, freq='D', tz='UTC')

#print(rng.tz_localize('Asia/Shanghai'))
#从单纯到本地化的转换是通过tz_localize方法处理的：
ts_utc = rng.tz_localize('UTC')
#print(ts_utc)
#一旦时间序列被本地化到某个特定时区，就可以用tz_convert将其转换到别的时区了：
#print(ts_utc.tz_convert('America/New_York'))

#tz_localize和tz_convert也是DatetimeIndex的实例方法：
ts = pd.Series(np.random.randn(len(rng)), index=rng)
#print(ts.index)
#print(ts.index.tz_localize('Asia/Shanghai'))


#srtftime的使用
