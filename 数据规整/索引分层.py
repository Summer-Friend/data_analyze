'''
@Author: your name
@Date: 2020-02-12 11:05:11
@LastEditTime: 2020-02-20 19:21:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\数据规整\1.py
'''
import numpy as np 
import pandas as pd

data = pd.Series(np.random.randn(9),
                  index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                         [1, 2, 3, 1, 3, 1, 2, 2, 3]])
#print(data)
#通过unstack方法将这段数据重新安排到一个完整的DataFrame中：
#print(data.unstack())
#unstack的逆运算是stack：
data.unstack().stack()

#可以实现分层索引
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                      columns=[['Ohio', 'Ohio', 'Colorado'],
                               ['Green', 'Red', 'Green']])
#各层也可以有名字
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
                    

#使用DataFrame的列进行索引########################################
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                       'c': ['one', 'one', 'one', 'two', 'two',
                             'two', 'two'],
                       'd': [0, 1, 2, 0, 1, 2, 3]})

#set_index函数会将其一个或多个列转换为行索引，并创建一个新的DataFrame：
frame2 = frame.set_index(['c', 'd'])
print(frame2)
#默认情况下，那些列会从DataFrame中移除，但也可以将其保留下来：
#frame.set_index(['c', 'd'], drop=False)

#reset_index
#https://blog.csdn.net/jingyi130705008/article/details/78162758?utm_source=distribute.pc_relevant.none-task
#reset_index可以还原索引，重新变为默认的整型索引 
frame3 = frame2.reset_index(level = ['c'])
print(frame3)

#sort_index:排序
obj=pd.Series([4,9,6,20,4],index=['d','a','e','b','c'])
#按obj的索引排序,默认升序，降序可在括号加ascending=False
print(obj.sort_index())