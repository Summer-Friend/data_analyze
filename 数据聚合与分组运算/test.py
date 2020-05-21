'''
@Author: your name
@Date: 2020-02-10 12:38:55
@LastEditTime: 2020-03-28 21:06:58
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\数据聚合与分组运算\test.py
'''
import pandas as pd
import numpy as np

people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

def peak_to_peak(arr):
    return arr.max() - arr.min()

print(people)
#print(people.apply(peak_to_peak))
print(people.agg(peak_to_peak))