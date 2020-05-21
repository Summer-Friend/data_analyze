'''
@Author: your name
@Date: 2020-02-18 16:10:41
@LastEditTime: 2020-02-19 11:24:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\Trump\test.py
'''
import pandas as pd 
import numpy as np 
from collections import Counter  


'''
data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':['2000-1-1','2001-1-2','2002-1-3','2001-1-4','2002-1-5'],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
data = pd.DataFrame(data)
#pandas也可以运用datetime模块的strptime函数，利用dt属性即可访问，但是先要to_datetime转换
#http://www.voidcn.com/article/p-kjkikhmw-bte.html
data['date'] = pd.to_datetime(data['year']).dt.strftime('%Y/%m/%d')
#print(data['date'])

#关于计数############################################
#GroupBy的size方法,任何分组关键词中的缺失值，都会被从结果中除去。
#size跟count的区别： size计数时包含NaN值，而count不包含NaN值
#print(data.groupby(['state']).size())
print(data['state'].count())
print(data['state'].value_counts())
#注意：'DataFrameGroupBy' object has no attribute 'value_counts'，也就是说分类过后无法用value_counts函数
#print(data.groupby(['state']).value_counts())


#维度
a = [[1,2,3],[4,5,6]]
a = pd.DataFrame(a)
print(a)
#直接用.shape可以快速读取矩阵的形状，使用shape[0]读取矩阵第一维度的长度(也就是行数)
print(a.shape)
#把dataframe变成list
print(a.values.tolist())

#读取csv的时候，第一行都会被认为是列索引
test = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\Trump\test.csv')
print(test)
print(list(test['1']))


#pandas.Series.str.lower
obj2 = pd.Series(['A','B','C','D'], index=['d', 'b', 'a', 'c'])
print(obj2.str.lower())


a = [1,4,2,3,2,3,4,2]  
b = Counter(a) #求数组中每个数字出现了几次
print(b)


a=pd.Series([0, 1, 0, 2])
print(a.shape)
'''
#map函数第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
print(list(map(str,list(range(10)))))
print(list(str(range(10)))