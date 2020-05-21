'''
@Author: your name
@Date: 2020-02-28 19:05:52
@LastEditTime: 2020-03-04 13:29:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\数据分析第二版\pandas\test.py
'''
import pandas as pd 
import numpy as np 

'''
iloc主要使用数字来索引数据，而不能使用字符型的标签来索引数据。
而loc则刚好相反，只能使用字符型标签来索引数据，不能使用数字来索引数据，
不过有特殊情况，当数据框dataframe的行标签或者列标签为数字，loc就可以来其来索引。
''' 

df=pd.DataFrame(np.arange(0,60,2).reshape(10,3),columns=list('abc'))
print(df.loc[0,['a', 'b']])

data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
data = pd.DataFrame(data)
#报错原因：https://blog.csdn.net/niuniuyuh/article/details/76650904
#print(data.loc[0,1])
#print(data.loc[:,[0,3]])
#print(data.iloc[0:3,'state'])
print(data.loc[0:3,'state'])
print(data.iloc[0:3,0:3])
print(data.iloc[:,[0,3]])
#print(data.iloc([0,3]))  这句是错的，因为参数没有指定完全

data.index = ['a','b','c','d','e']
#报错原因：https://blog.csdn.net/niuniuyuh/article/details/76650904
#print(data.loc[0:3,'state'])
print(data.loc['a'])
print(data.loc[['a','b'], 'state'])