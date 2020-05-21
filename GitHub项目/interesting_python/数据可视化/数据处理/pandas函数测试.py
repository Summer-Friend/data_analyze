'''
@Author: your name
@Date: 2020-01-31 14:21:38
@LastEditTime : 2020-02-04 20:11:56
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\数据可视化\数据处理\函数使用.py
'''
import pandas as pd
import numpy as np
from numpy import nan as NaN

'''
#填充函数
df1=pd.DataFrame([[1,2,3],[NaN,NaN,2],[NaN,NaN,NaN],[8,8,NaN]])
print(df1)

#1.用常数填充
print (df1)
print ("-----------------------")
print (df1.fillna(100))

#2.用字典填充
print ("-----------------------")
print(df1.fillna({0:10,1:20,2:30}))

#二、指定inplace参数
修改一个对象时：
        inplace=True：不创建新的对象，直接对原始对象进行修改；
        inplace=False：对数据进行修改，创建并返回新的对象承载其修改结果。
        默认是False，即创建新的对象进行修改，原对象不变，和深复制和浅复制有些类似。

print (df1.fillna(0,inplace=False))  #所以这个地方才会返回None，已经对df1进行了修改
print ("-------------------------")
print (df1)

#.iloc使用全是以0开头的行号和列号，不能直接用其它索引,.loc只选取行
#三、指定method参数
df2 = pd.DataFrame(np.random.randint(0,10,(5,5)))
print(df2)
print ("-------------------------")
df2.iloc[1:4,3] = NaN
df2.iloc[2:4,4] = NaN
print(df2)
print ("-------------------------")
#1.method = 'ffill'/'pad'：用前一个非缺失值去填充该缺失值
#print(df2.fillna(method='ffill'))
#2.method = 'bflii'/'backfill'：用下一个非缺失值填充该缺失值
#print(df2.fillna(method='bfill'))
'''

#针对行列的操作
df3 = pd.DataFrame({'a':[0,1,2,3],'b':[4,5,6,7],'c':[8,9,10,11],'d':[12,13,14,15]})
#df3.iloc[1:4,2] = NaN
#df3.iloc[2:4,3] = NaN
#df3.loc[1:4,2] = NaN
#df3.loc[2:4,3] = NaN
print(df3['a'].head())
#print(df3['b'])
#选取第二行和第四行
#print(df3.loc[1,3])
#第二行第四列
#print(df3.iloc[1,3])
#第二行到第三行
#print(df3.iloc[1:3])
#集体请参考：https://zhuanlan.zhihu.com/p/29720778