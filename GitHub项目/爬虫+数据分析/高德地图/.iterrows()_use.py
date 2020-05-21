'''
@Author: your name
@Date: 2020-02-02 14:42:14
@LastEditTime : 2020-02-02 14:50:01
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\爬虫+数据分析\高德地图\.iterrows()_use.py
'''
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
#for循环定义了两个变量，index，row，那么返回的元组，index=index，row=row.
#在需要遍历行数据的时候，就可以使用 iterrows()方法实现
for index, row in df.iterrows():
   print(index)
   print(row)