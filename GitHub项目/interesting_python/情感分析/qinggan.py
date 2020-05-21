'''
@Author: your name
@Date: 2020-01-30 20:17:56
@LastEditTime : 2020-01-30 20:27:35
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\情感分析\qinggan.py
'''
import numpy as np
import pandas as pd
data = pd.read_csv('E:\\vscode_code\\GitHub项目\\interesting_python\\情感分析\\data.csv')
print(data.head())
def make_label(star):
    if star > 3:
        return 1
    else:
        return 0
    
data['sentiment'] = data.star.apply(make_label)
print(data['sentiment'].head())
print(data.head())
#data_wx = pd.concat(data,data['sentiment'])