'''
@Author: your name
@Date: 2020-02-12 21:43:15
@LastEditTime: 2020-04-01 10:53:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\数据规整\2.py
'''
import pandas as pd 

"""
#这两个：一、concat：沿着一条轴，将多个对象堆叠到一起；二、merge：通过键拼接列，是对于dataframe的合并

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,  
      keys=None, levels=None, names=None, verify_integrity=False, copy=True)

#https://blog.csdn.net/brucewong0516/article/details/82707492
#https://blog.csdn.net/gdkyxy2013/article/details/80785361
"""

"""
#str.cat是针对于拼接而非合并
data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
data = pd.DataFrame(data)

data['a'] = data['state'].str.cat(data['salary'], sep = '-')
#强制转化成了str之后就可以合并了
data['year_str'] = data['year'].astype('str')
data['b'] = data['state'].str.cat(data['year_str'], sep = '-')
print(data)
"""

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                       'A': ['A0', 'A1', 'A2', 'A3'],
                       'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
#result = pd.concat([left['A'], right['C']], axis = 1)
result = pd.concat(left['A'], right['C'], left_index=True, right_index=True, how='outer')
print(result)
