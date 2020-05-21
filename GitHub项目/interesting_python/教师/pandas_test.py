'''
@Author: your name
@Date: 2020-01-30 19:58:46
@LastEditTime : 2020-01-30 23:11:08
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\测试\pandasss.py
'''
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
'''
df1 = pd.DataFrame({ 'a':[0,0,0], 'b': [1,1,1]})
df2 = df1.copy()
df2['a'] = df2['a'] + 1
print('df1:',df1,'df2:',df2)
'''
data={'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',
       '5000K/MTH - 20000K/MTH', '12K/MTH - 19K/MTH',
       '4000K/MTH - 6000K/MTH', '14000K/MTH - 22000K/MTH','8000K/MTH - 20000K/MTH']}

data_jlc = pd.DataFrame(data)
#data_jlc = data.info()
print(data_jlc)

def get_salary_jlc(data):
    pat_jlc = r"(.*)K/MTH - (.*)K/MTH"
    if '00' in data:
        low, high = re.findall(pattern=pat_jlc, string=data)[0]
        return (float(low)+float(high))/2/1000
    else:
        low, high = re.findall(pattern=pat_jlc, string=data)[0]
        return (float(low)+float(high))/2

#???DataFrame?apply????????????DataFrame??;????CSV???pandas?????????????
data_jlc['salary_clean'] = data_jlc['salary'].apply(get_salary_jlc)
print(data_jlc['salary_clean'])

#print(data_jlc['salary'].apply(get_salary_jlc))