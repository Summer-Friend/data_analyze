'''
@Author: your name
@Date: 2020-02-06 20:02:49
@LastEditTime : 2020-02-06 20:31:24
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\爬虫+数据分析\猫眼\数据分析.py
'''
import pandas as pd
import numpy as np

data = pd.read_csv(r'E:\vscode_code\GitHub项目\爬虫+数据分析\猫眼\maoyan.csv',encoding='utf-8')
#print(data['star'].mean())
data['year'] = data['pub_time'].str.split('-').str[1]
data['month'] = data['pub_time'].str.split('-').str[1]
#print(data.head())
year = data.groupby('year')['year'].count()
month = data.groupby('month')['month'].count()

from pyecharts import Line

attr = list(year.index)
v = list(year)
line = Line("电影年份分布情况")
line.add("", attr, v, mark_point=["average"])
line.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\猫眼\电影年份分布情况.html')


from pyecharts import Bar

attr = list(month.index)
v = list(month)
bar = Bar("")
bar.add("", attr, v)
bar.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\猫眼\电影月份分布情况.html')

def get_country(i):
    country = i.split('(')
    if len(country) == 1:
        return '中国'
    else:
        #先split拆掉左括号，再用strip忽略掉右括号
        #str.strip([chars]);用法：chars -- 移除字符串头尾指定的字符序列。返回移除字符串头尾指定的字符生成的新字符串。
        country_1 = country[1].strip(')')
        if country_1 == '中国香港':
            return '中国'
        elif country_1 == '法国戛纳':
            return '法国'
        else:
            return country_1
        
#map() 会根据提供的函数对指定序列做映射。
# 对data['pub_time']全部使用get_country函数，与apply类似，但apply一般用于数据分组后再进行函数套用
data['country'] = data['pub_time'].map(get_country)
#如果直接使用，只能对单独元素进行操作
#print(data['pub_time'][0].split('('))
#data.head()
country = data.groupby('country')['country'].count()

from pyecharts import Pie

attr = list(country.index)
v1 = list(country)
pie = Pie("", title_pos='center')
pie.add(
    "",
    attr,
    v1,
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
pie.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\猫眼\电影国家分布情况.html')


#提取人名
str = ''
for i in range(100):
    str = str + data.iloc[i,1] + ','
author = str.split(',')


from collections import Counter
c = Counter(author)
#collection内的函数，和pandas的nlargest有点像
count = c.most_common(6)
attr = []
v = []
for i in count:
    attr.append(i[0])
    v.append(i[1])
    
from pyecharts import Bar
bar = Bar("")
bar.add("", attr, v)
bar.render(r'E:\vscode_code\GitHub项目\爬虫+数据分析\猫眼\明星上榜情况.html')
