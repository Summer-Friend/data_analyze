'''
@Author: your name
@Date: 2020-02-18 10:25:29
@LastEditTime: 2020-02-18 16:11:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\English_name\test.py
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import Bar, Line, Overlap

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  #解决seaborn中文字体显示问题
plt.rc('figure', figsize=(10, 10))  #把plt默认的图片size调大一点

data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2015,1.7,2032,2041,2052],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
data = pd.DataFrame(data)

#挑选最大值的时候要指定某一列，不然报错
data_clean = data.groupby(['state','pop','salary']).year.sum()
#print(data_clean)
#print(data_clean.groupby(level = [1,2]).nlargest(2))
#print(data_clean.year.nlargest(1))

b = [2010,2020,2030,2040,2050,2060]
c = ['10后', '20后', '30后', '40后', '50后']
data['decade'] = pd.cut(data['year'], b)


#多重索引
df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'])
#print(df)


#索引的index
#drop指是否把原来的列给删了
data_index = data.set_index('state', drop = True)
#print(data_index)
data_index2 = data_clean.reset_index(level = [0,1], drop = True)
#print(data_index2)

#dataframe支持相除等运算
#print((data['year']/data['pop']).round(2))


#set用法，去重
a = [1,1,2,3,4]
b = [0,1,2,3,6]
print(set(a) & set(b))


#
data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2015,1.7,2032,2041,2052],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
data = pd.DataFrame(data)
#print(data['pop'].mean())
#print(data['pop'].unique() & data['year'].unique())
print(data.iloc[0])

data_clean2 = list(set((data['pop'].unique())) & set((data['year'].unique())))
#data_clean3 = list((data['pop'].unique())) & list(data['year'].unique())
#print(data_clean2)
#print(data.pivot(index = 'state', columns = 'year', values = 'pop'))