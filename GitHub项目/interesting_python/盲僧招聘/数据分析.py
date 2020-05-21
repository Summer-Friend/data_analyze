'''
@Author: your name
@Date: 2020-02-03 14:20:40
@LastEditTime : 2020-02-03 15:07:34
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\盲僧招聘\分析.py
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyecharts
from pylab import mpl
data_dm = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\盲僧招聘\datamining.csv')
data_ml = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\盲僧招聘\machinelearning.csv')
data_al = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\盲僧招聘\mlalgorithm.csv')
#依然保留索引
data = pd.concat([data_dm, data_ml, data_al], ignore_index = True)
#print(data.loc[666])
#去重
data.drop_duplicates(subset='job_links', inplace=True)
print(data.shape)
#axis是为了确定要删的标签是属于column还是index，0代表按照index，1代表按照列
data_clean = data.drop(['com_id', 'com_links', 'com_location', 'com_website', 
                 'com_welfare', 'detailed_intro', 'job_detail'], axis = 1)

print(data['auth_capital'].sample(5))
auth_capital = data['auth_capital'].str.split('：', expand = True)
print(auth_capital.sample(5))

#Series.str.extract(pat, flags=0, expand=None) 参数: pat : 字符串或正则表达式 flags : 整型, expand : 布尔型,是否返回DataFrame
auth_capital['num'] = auth_capital[1].str.extract('([0-9.]+)', expand=False).astype('float')
print(auth_capital.sample(5))

#以“万”字分割字符串，便可把数值和币种分开来
print(auth_capital[1].str.split('万', expand = True)[1].unique())

#为了过程更好理解，可以先新建一个“ex_rate”（汇率）列，保存对应的汇率
def get_ex_rate(string):
    if string == None:
        return np.nan
    if '人民币' in string:
        return 1.00
    elif '港' in string:
        return 0.80
    elif '美元' in string:
        return 6.29
    elif '欧元' in string:
        return 7.73
    elif '万' in string:
        return 1.00
    else:
        return np.nan
    
auth_capital['ex_rate'] = auth_capital[1].apply(get_ex_rate)
auth_capital.sample(5)
data_clean['auth_capital'] = auth_capital['num'] * auth_capital['ex_rate']
data_clean['auth_capital'].head()