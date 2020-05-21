'''
@Author: your name
@Date: 2020-02-10 12:40:36
@LastEditTime: 2020-02-18 21:24:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\数据聚合与分组运算\课件.py
'''
import pandas as pd
import numpy as np

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
#group之后只是一个对象，可以对这个对象进行一系列操作
grouped = df['data1'].groupby(df['key1'])
means = df['key2'].groupby(df['key1'])
count = df['key1'].groupby(df['key2'])
#print(means)

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
#print(df['data1'].groupby([states]).mean())

#GroupBy的size方法,任何分组关键词中的缺失值，都会被从结果中除去。
#size跟count的区别： size计数时包含NaN值，而count不包含NaN值
#https://www.cnblogs.com/zknublx/p/12048410.html
print(df.groupby(['key1', 'key2']).size())

"""
#GroupBy对象支持迭代，可以产生一组二元元组（由分组名和数据块组成）
for name,group in grouped:
    print(name)
    print(group)
""" 
   
#mapping传递
people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
#你可以计算一个字符串长度的数组，更简单的方法是传入len函数：
#print(people.groupby(len).sum())

mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f' : 'orange'}

by_column = people.groupby(mapping, axis=1)
by_column.sum()

#Series也有同样的功能，它可以被看做一个固定大小的映射：
map_series = pd.Series(mapping)

#聚合的话可以用apply或agg传入函数，见test
