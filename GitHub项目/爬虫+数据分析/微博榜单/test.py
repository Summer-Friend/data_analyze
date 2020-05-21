'''
@Author: your name
@Date: 2020-02-20 19:00:54
@LastEditTime: 2020-02-20 19:15:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\爬虫+数据分析\微博榜单\test.py
'''
import pandas as pd 


a = 'xu yi fan'
print(a.split(' ')[0])
b = {1:['x', 'y', 'f']}
#print(b[1].str.split(' '))

data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
data = pd.DataFrame(data)

#series类型数据需要先经过str处理
#注意下面的区别
print(data['salary'].str.split('-')[0])
print(data['salary'].str.split('-').str[0])