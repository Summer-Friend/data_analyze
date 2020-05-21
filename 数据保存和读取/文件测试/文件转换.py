'''
@Author: your name
@Date: 2020-02-22 21:52:21
@LastEditTime: 2020-03-28 20:25:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\文件测试\文件转换.py
'''
#https://www.jianshu.com/p/ab0c62ee002b
import pandas as pd
'''
data = pd.read_excel(r'E:\vscode_code\数据分析第二版\数据保存\文件测试\test.xlsx','Sheet1',index_col=0)
data.to_csv(r'E:\vscode_code\数据分析第二版\数据保存\文件测试\test.csv',encoding='utf-8')
'''
#这个时候一定要加'header=None', 这样读进来的列名就是系统默认的0，1，2... 序列号
data = pd.read_csv(r'E:\vscode_code\数据分析第二版\数据保存\文件测试\test.csv', header=None)
print(data)
#设置列标和索引
data.columns = ['a','b']
data.index = ['c','d','e']
print(data)