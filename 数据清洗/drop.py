'''
@Author: your name
@Date: 2020-02-13 10:25:55
@LastEditTime: 2020-03-02 11:04:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\数据清洗\test.py
'''
#https://blog.csdn.net/luocheng7430/article/details/80330566
#drop方法
import numpy as np 
import pandas as pd

print(chr(ord('a')+1))

data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
data = pd.DataFrame(data)
clean = data.drop(data[data['year'] == 2000].index)
print(clean)
#下面这句和clean效果一样
print(data[data['year'] != 2000])
print(data[data['year'] == 2000].index)
