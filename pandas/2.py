'''
@Author: your name
@Date: 2020-02-17 11:54:40
@LastEditTime: 2020-02-28 13:31:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\pandas\2.py
'''
import numpy as np; import pandas as pd


values = pd.Series([0, 1, 0, 2] * 2)
dim = pd.Series(['apple', 'orange','banana'])

#可以使用take方法存储原始的字符串Series：
#用于分类，但是values和dim里面的类别数量必须相等，否则报错
#print(dim.take(values))

#
fruits = ['apple', 'orange', 'apple', 'apple'] * 2

N = len(fruits)
df = pd.DataFrame({'fruit': fruits,
                   'basket_id': np.arange(N),
                   'count': np.random.randint(3, 15, size=N),
                   'weight': np.random.uniform(0, 4, size=N)},
                  columns=['basket_id', 'fruit', 'count', 'weight'])

#dtypes(查询数据类型) 、astype(强制转换数据类型)
fruit_cat = df['fruit'].astype('category')
#print(fruit_cat)

#GroupBy高级应用#################################
df = pd.DataFrame({'key': ['a', 'b', 'c'] * 4,
                   'value': np.arange(12.)})

g = df.groupby(df['key'])
print(g.mean())

#重采样
df = pd.DataFrame({'time': np.arange(N * 3.),
                    'key': np.tile(['a', 'b', 'c'], N),
                    'value': np.arange(N * 3.)})
print(df)
print(df.set_index('key'))


#下面用法自行体会
data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
data1 = pd.DataFrame.from_dict(data)
data2 = pd.DataFrame(data)
data3 = pd.DataFrame.from_dict(data, orient='index',
                       columns=['A', 'B', 'C', 'D'])
print(data1)
print(data2)
print(data3)
