'''
@Author: your name
@Date: 2020-02-07 17:44:47
@LastEditTime : 2020-02-15 10:24:25
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\爬虫+数据分析\丁香医生\函数测试.py
'''
import pandas as pd 
import numpy as np
'''
#提供数组
grade_same1 = np.round(np.array([3, 31, 12, 1, 0]) / (3+31+12+1)*100, 1)
print(grade_same1)

a=(1,2,3)
grade_same2 = list(a)/2
print(grade_same2)
'''
data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
data = pd.DataFrame(data)
#根据state字段进行去重，inplace参数表示是否修改原对象
#print(data.drop_duplicates(subset='state',inplace = False))
#print(data)
#print(data.loc[data['state']!='Ohio1','year'])
#str.contains对于整型没用  比如：#print(data.loc[data['pop'].str.contains(1.5),'year'])报错
#print(data.loc[data['state'].str.contains('Ohio1|Ohio2')&data['salary'].str.contains('7K/MTH - 8K/MTH'),'year'])
