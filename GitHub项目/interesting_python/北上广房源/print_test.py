'''
@Author: your name
@Date: 2020-02-05 11:18:24
@LastEditTime : 2020-02-14 16:47:36
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\北上广房源\print_test.py
'''
import scipy
import numpy as np  
import pandas as pd
x=1
y=2
z='a'
df1 = pd.DataFrame({ 'a':[0,0,0], 'b': [1,1,1]})
#print(x,'|',y)
#print(x+'|'+y)
#print(z+'|'+'b')
#print(str(x)+z)
#df1.to_csv(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\{}.csv'.format(str(x)+z))
data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\北上广房源\data_clean.csv')
#print(data['rent_price_listing'].head())
print(data['house_tag'].sample(20))
sh_tag = []
for st in data[data['city']=='上海'].dropna(subset=['house_tag'])['house_tag']:
    sh_tag.extend(st.split(' '))
#print(sh_tag)