'''
@Author: your name
@Date: 2020-02-19 10:07:50
@LastEditTime: 2020-02-19 10:18:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\数据分析第二版\数据保存\1.py
'''
import pandas as pd


data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
data2 = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
data3 = {
    'state2':['Ohio2','Ohio2','Ohio2','Nevada2','Nevada2'],
    'year2':[2002,2012,2022,2012,2022],
    'pop2':[1.52,1.72,3.62,2.42,2.92],
    'salary2':['5000K/MTH - 20000K/MTH', '12K/MTH - 19K/MTH',
       '4000K/MTH - 6000K/MTH', '14000K/MTH - 22000K/MTH','8000K/MTH - 20000K/MTH']
}
data = pd.DataFrame(data)
data2 = pd.DataFrame(data2)
data3 = pd.DataFrame(data3)

#第一： 一定要使用header = false, 不然的话保存数据集的时候，会自动使用0-n作为数据的列名。但如果是字典，就使用键值当索引
#第二： 一定也要使用index=False, 不然的话保存数据的时候，会自动加上一个索引列。
#第三： 如果不需要覆盖原文件， 用mode='a'，默认是覆盖原文件的
#这里因为是字典带有键值，所以还是header=true，但是如果需要

data.to_csv(r'E:\vscode_code\数据分析第二版\数据保存\1.csv', index=False, header=True)
data2.to_csv(r'E:\vscode_code\数据分析第二版\数据保存\1.csv', index=False, mode='a', header=False)
data3.to_csv(r'E:\vscode_code\数据分析第二版\数据保存\1.csv', index=False, mode='a', header=False)