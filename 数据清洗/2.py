'''
@Author: your name
@Date: 2020-02-11 13:18:33
@LastEditTime : 2020-02-11 20:05:45
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\数据清洗\2.py
'''
import pandas as pd
import numpy as np 
from numpy import nan as NA

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
#检查缺失数据，返回布尔值
#print(string_data.isnull())

string_data[0] = None
#print(string_data.isnull())

#清洗###############################
#对于DataFrame对象，事情就有点复杂了。你可能希望丢弃全NA或含有NA的行或列。dropna默认丢弃任何含有缺失值的行：
#滤除缺失数据
#print(string_data.dropna())

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
#传入how='all'将只丢弃全为NA的那些行：
cleaned2 = data.dropna(how='all')
#用这种方式丢弃列，只需传入axis=1即可
cleaned3 = data.dropna(axis=1, how='all')

#填充################################
data.fillna(0)
#若是通过一个字典调用fillna，就可以实现对不同的列填充不同的值：
data.fillna({1: 0.5, 2: 0})
#默认返回新对象，若对现有对象修改，用inplace参数
data.fillna(0, inplace=True)
#里面还有别的参数可以了解

#替换#################################
#map可用于修改对象的数据子集，而replace则提供了一种实现该功能的更简单、更灵活的方式
data = pd.Series([1., -999., 2., -999., -1000., 3.])
#一次性替换多个值，可以传入一个由待替换值组成的列表以及一个替换值
data.replace([-999, -1000], np.nan)
#要让每个值有不同的替换值，可以传递一个替换列表：
data.replace([-999, -1000], [np.nan, 0])
#传入的参数也可以是字典：
data.replace({-999: np.nan, -1000: 0})

#重命名轴索引##########################
data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
#1.
transform = lambda x: x[:4].upper()
data.index.map(transform)
#data.rename()#内置参数

#离散化和面元划分#############################
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages,bins)
#print(pd.value_counts(cats))
#你可以通过传递一个列表或数组到labels，设置自己的面元名称：
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins, labels=group_names)
#qcut是一个非常类似于cut的函数，它可以根据样本分位数对数据进行面元划分。


#检测和过滤异常值,一般就依靠算法了#####################
#生成4组，每一组包含1000个元素,numpy.random.rand()则相反
data = pd.DataFrame(np.random.randn(1000, 4))
#print(data[2][np.abs(data[2])>3])
#print(data[(np.abs(data) > 3).any(1)])

#字符串对象方法###########################
val = 'a,b,  guido'
val1 = val.split(',')
#strip方法不支持列表操作
pieces = [x.strip() for x in val.split(',')]
print(val1,' ',pieces)
#可以直接赋值
first, second, third = pieces
#下面两种方法一样
first + '::' + second + '::' + third
'::'.join(pieces)

