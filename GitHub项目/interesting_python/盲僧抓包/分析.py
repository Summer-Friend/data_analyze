'''
@Author: your name
@Date: 2020-02-28 11:43:54
@LastEditTime: 2020-02-28 11:50:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\盲僧抓包\分析.py
'''
import pandas as pd 

data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\盲僧抓包\com_detailed.csv')
data = data[data['com_type'].isin(['有限责任公司(自然人投资或控股)',
                     '有限责任公司' '有限责任公司(法人独资)'])].groupby(['reg_name']).size().reset_index()
print(data)
