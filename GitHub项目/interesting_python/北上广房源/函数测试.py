'''
@Author: your name
@Date: 2020-02-05 18:32:42
@LastEditTime : 2020-02-14 10:03:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\北上广房源\函数测试.py
'''
import requests
import json
import numpy as np
import pandas as pd
from collections import Counter
from pyecharts import WordCloud
 
'''
#split测试
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print (str.split( ))       # 以空格为分隔符，包含 \n
print (str.split(' ', 1 )) # 以空格为分隔符，分隔成两个


#str.extract ()测试
data = {
    'state':['Ohio2','Ohio2','Ohio2','Nevada2','Nevada2'],
    'year':[2002,2012,2022,2012,2022],
    'pop':[1.52,1.72,3.62,2.42,2.92],
    'salary':['5000K/MTH - 20000K/MTH', '12K/MTH - 19K/MTH',
       '4000K/MTH - 6000K/MTH', '14000K/MTH - 22000K/MTH','8000K/MTH - 20000K/MTH'],
    'another':['a123b','a234b','a345b','a456b','a567b']
}
frame = pd.DataFrame(data)
#切片
#print(frame['state'].str[2:])
#print(frame['state'].str[:2])
#str.extract()函数和正则表达式相当于是更高级的切片法则
#这个正则匹配不知道为啥还得加括号
print(frame['another'].str.extract('(\d+.+\d)'))
print(frame['state'].str.extract("(.+\d)"))


#Counter测试，即计算各元素出现次数，中文会有所不同
st = "1a,2b,3c,aa,bb,cc,22,33,11,ab,ac,bc"
st2 = ['你我他', '你和我', '她和你','你我', '他他他', '你我他']
counter = Counter(st)  # 字符计数
print(counter)
counter2 = Counter(st2)  # 字符计数
print(counter2)
#print(WordCloud.cast(Counter(st2)))


#cast函数测试，在wordcould中用于计算词云，在counter的基础上将元素和出现次数分开存放，形成两个列表
st3 = {'集中供暖': 2434, '近地铁': 1782, '随时看房': 1562, '精装': 1256, '新上': 665, '双卫生间': 399, '月租': 16, '押一付一': 5}
print(WordCloud.cast(Counter(st3)))
'''

'''
#test false
#关于json提取数据可参照：E:\vscode_code\vscode_python_test\练习\json测试\json应用.py
data = {
    'state':['Ohio2','Ohio2','Ohio2','Nevada2','Nevada2'],
    'year':[2002,2012,2022,2012,2022],
    'pop':[1.52,1.72,3.62,2.42,2.92],
    'salary':['5000K/MTH - 20000K/MTH', '12K/MTH - 19K/MTH',
       '4000K/MTH - 6000K/MTH', '14000K/MTH - 22000K/MTH','8000K/MTH - 20000K/MTH']
}

item  = {'another':['a123b','a234b','a345b','a456b','a567b']}
print(item)
for rec in data:
    #item['bedroom_num'] = rec.get('state')
    item['hall_num'] = rec.get('year')
    item['bathroom_num'] = rec.get('pop')
    #item['rent_area'] = rec.get('salary')

print(item)


 
#请求地址
url = "https://api.global.net/datastore/v1/tracks/"
#发送get请求
r = requests.get(url)
#获取返回的json数据
 
print(r.json())
'''

#数据筛选,dropna和loc拓展
data = {
    'state':['Ohio2','Ohio2','Ohio2','Ohio2','Nevada2'],
    'year':[2002,2012,2019,2012,2022],
    'pop':[None,1.72,' ',2.42,2.92],
    'salary':['5000K/MTH - 20000K/MTH', '12K/MTH - 19K/MTH',
       '4000K/MTH - 6000K/MTH', '14000K/MTH - 22000K/MTH','8000K/MTH - 20000K/MTH']
}
data = pd.DataFrame(data)  

#函数测试,这个玩意儿很重要，因为dropna对缺失值才有效果，对空值是没用的
def dw_None_latlon(data):
    if data is None or data == '' or data == ' ':
        return np.nan
    else:
        return float(data)     

data['pop'] = data['pop'].apply(dw_None_latlon)
#print(data['pop'])

data['latitude'] = data['state'].astype(str)
data['latlon'] = data['salary'].str.cat(data['latitude'], sep=',')

col = ['year','salary','pop']
#loc所对应的分别是行列的筛选条件，dropna只能对已经筛选出的数据进行清理
data_latlon = data.loc[(data['state']=='Ohio2')&(data['year']<=2020), col].dropna(subset=['pop'])
data_latlon2 = data.dropna(subset = ['pop'])['pop']
print(data_latlon)
print(data_latlon2)


