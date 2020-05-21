'''
@Author: your name
@Date: 2020-03-08 17:52:50
@LastEditTime: 2020-03-30 15:38:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\数据分析第二版\pandas函数\test.py
'''
import pandas as pd 
import numpy as np 

data = {'a':['1','2','3'],'b':['4','5','6']}
data = pd.DataFrame(data)
print(data)

#这是修改两种数据类型的方法
data['c'] = pd.to_numeric(data['a']*4, errors='coerce')
print(data.iloc[2,2])
print(type(data.iloc[2,2]))
data['b'] = data['b'].astype('int64')
print(data.iloc[2,1])
print(type(data.iloc[2,1]))

data['c'].astype('int32')
print(type(data.iloc[2,2]))
'''
#所有元素的累计和
print(data['a'].astype('int64').sum())
print(data['a'].cumsum())
print(data['a'].astype('int64').sort_values(ascending = False))
'''
print(data['b'].notnull().sum())
#第a列索引为2的元素
print(data.a[2])