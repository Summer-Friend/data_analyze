'''
@Author: your name
@Date: 2020-02-10 20:02:42
@LastEditTime: 2020-02-28 19:12:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\pandas\1.py
'''
import pandas as pd
import numpy as np


obj = pd.Series([4, 7, -5, 3])
#print(obj)
obj.values
obj.index

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
#print(obj2[['c', 'a', 'd']])
obj2[obj2 > 0]
np.exp(obj2)
#print('b' in obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
#单个元素的字典直接转为DataFrame时，程序会报错，需要适当做些转换，指定行索引或者列索引才行
#sdata2 = {'Ohio': [35000], 'Texas': [71000], 'Oregon': [16000], 'Utah': [5000]}
#obj4 = pd.DataFrame(sdata2)
#print(obj3)
#print(obj4)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)

#pandas的isnull和notnull函数可用于检测缺失数据：
pd.isnull(obj4)
pd.notnull(obj4)
#Series也有类似的实例方法：
obj4.isnull()

#reindex，其作用是创建一个新对象，它的数据符合新的索引
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])

#利用标签的切片运算与普通的Python切片运算不同，其末端是包含的：
#print(obj['b'])
#print(obj[['b','c']])
#print(obj['b':'c'])

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                index=['Ohio', 'Colorado', 'Utah', 'New York'],
                columns=['one', 'two', 'three', 'four'])

#用loc和iloc进行选取
#使用轴标签（loc）或整数索引（iloc），从DataFrame选择行和列的子集。
#选取行索引用loc，列索引用iloc
#print(data)
print(data.loc[0, ['one']])
#print(data.loc['Colorado', ['two', 'three']])
#print(data.loc[:, 'one'])
#print(data.iloc[2, [3, 0, 1]])
#print(data.iloc[2])
#print(data.iloc[[1, 2], [3, 0, 1]])

#这两个索引函数也适用于一个标签或多个标签的切片：
#print(data.loc[:'Utah', 'two'])
#上下两种用法一样
#print(data.iloc[:, :3][data.three > 5])
#print(data.iloc[:, :3][data['three']>5])

#pandas可以对不同索引的对象进行算术运算。在将对象相加时，如果存在不同的索引对，则结果的索引就是该索引对的并集。
s1 = pd.Series([7.3, -2.5, '', 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],index=['a', 'c', 'e', 'f', 'g'])
#print(s1 + s2)

#使用df1的add方法，传入df2以及一个fill_value参数,就是一个填充值，不然会用NaN代替
#print(s1.add(s2,fill_value = 0))

#DataFrame和Series之间的运算要注意，是每一行或每一列都会进行运算

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
np.abs(frame)  #求绝对值

#声明匿名函数
f = lambda x: x.max() - x.min()
#这里的函数f，计算了一个Series的最大值和最小值的差
#在frame的每列都执行了一次。结果是一个Series，使用frame的列作为索引
frame.apply(f)

#如果传递axis='columns'到apply，这个函数会在每行执行：
frame.apply(f, axis='columns')

#排序和排名
obj = pd.Series(range(4), index=['b', 'a', 'b', 'c'])
obj.sort_index()
#索引的is_unique属性可以告诉你它的值是否是唯一的：
#print(obj.index.is_unique)

#extract使用  #https://blog.csdn.net/claroja/article/details/64929819
#如果提取的规则结果有多组，则会返回数据框，不匹配的返回NaN
s3 = pd.Series(['a1', 'b2', 'c3'])
print(pd.Series(s3).str.extract('([ab])(\d)', expand=False))
print(pd.Series(['a1', 'b2', 'c3']).str.extract('([ab])(\d)', expand=False))





