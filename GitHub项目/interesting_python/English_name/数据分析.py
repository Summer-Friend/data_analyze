'''
@Author: your name
@Date: 2020-02-18 10:19:02
@LastEditTime: 2020-02-18 16:09:04
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\English_name\数据分析.py
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import Bar, Line, Overlap, WordCloud

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  #解决seaborn中文字体显示问题
plt.rc('figure', figsize=(10, 10))  #把plt默认的图片size调大一点

data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\English_name\Names_sample.csv')

"""
#1.2010-2017年，Top15的男生、女生英文名###################################################
#注意：这个Count是指代'Count'这一列，而不是个函数啥的
top15_boy = data.loc[(data['Year'].isin(list(range(2010,2018)))) & (data['Gender'] == 'M'), :].groupby('Name').Count.sum().nlargest(15)
boy_total = data.loc[(data['Year'].isin(list(range(2010,2018)))) & (data['Gender'] == 'M'), :].groupby('Name').Count.sum().sum()

#点云
name = list(top15_boy.index)
value = list(top15_boy.values)
wordcloud = WordCloud(width=800, height=450,background_color='#f2eada')  # feeeed
wordcloud.add("", name, value, word_size_range=[20, 100],shape='diamond')
wordcloud.render(r'E:\vscode_code\GitHub项目\interesting_python\English_name\top15_boy.html')


data_top15_boy = data.loc[(data['Year'].isin(list(range(2010,2018)))) & (data['Gender'] == 'M') & 
                          (data['Name']).isin(list(top15_boy.index)), :]
data_top15_boy.sort_values(by = ['Year', 'Count'], ascending=False, inplace=True)


#seaborn的可视化，自己去了解
sns.set(font_scale=1.4)
g = sns.FacetGrid(data_top15_boy, col="Name", col_wrap=3)

g = g.map(plt.plot, "Year", "Count",color="c",marker=".")
g.set(facecolor='#f2eada')
#plt.show()


#2. 每个年代，最流行的英文名字,1920-2017#############################################
data_decades = data[data['Year']>=1920]
#labels就是分区所替换的名称,不加的话就是用区间代替了
data_decades['decade'] = pd.cut(data_decades['Year'], [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2018], 
                                labels = ['20后','30后','40后', '50后','60后','70后','80后','90后','00后','10后'],right=False)
decade = data_decades.groupby(['decade', 'Gender', 'Name']).Count.sum().groupby(level=[0,1]).nlargest(1)
#print(decade)
#print(decade.index.get_level_values(2))
#在获取多重索引用到
decade_boy_count = decade.iloc[decade.index.get_level_values(3)=='M'].reset_index(level=[0,1,3], drop=True)
#print(decade_boy_count)
decade_boy_total = data_decades[data_decades['Gender']=='M'].groupby('decade').Count.sum()
#print(decade_boy_total)
decade_boy_pct = (decade_boy_count/decade_boy_total*100).round(2)
ax = decade_boy_pct.plot.barh(title='各年代最流行的男性名字')
ax.set_ylabel('')
ax.set_xlabel('百分比')
ax.set(facecolor='#f2eada')
#plt.show()


#3. 以前很流行，现在不流行的名字#########################################
data_popular_former = data[(data['Year'] < 1950) & (data['Count'] > 10500) & (data['Gender'] == 'M')]
data_not_popular_now = data[(data['Year'] > 2000) & (data['Count'] < 1000) & (data['Gender'] == 'M')]
#第二个list可加可不加，unique之后自动返回列表
boys_names_popular_former = list(set(list(data_popular_former.Name.unique())) & set(list(data_not_popular_now.Name.unique())))
print(set(list(data_popular_former.Name.unique())))
#print(data_popular_former.Name.unique() & data_not_popular_now.Name.unique())
#print(boys_names_popular_former)
boys_names_popular_former_data = data[(data['Name'].isin(boys_names_popular_former)) & (data['Year']>=1920) & (data['Gender']=='M')]
attr = list(range(1920, 2018))


#4. 2000年后越来越流行的名字#######################################
data_popular_now = data[(data['Year']>=2000)&(data['Gender'] =='M')&(data['Count']>7000)]
#pivot()方法进行重新排列
data_popular_now = data_popular_now.pivot(index='Name', columns='Year',values='Count')
#print(data_popular_now)
year = pd.DataFrame({'Year':list(range(2000, 2018))}, index=list(range(2000, 2018)))
#pandas.DataFrame.corrwith用于计算DataFrame中行与行或者列与列之间的相关性。axis代表行或列
#https://blog.csdn.net/w1301100424/article/details/98473560
data_popular_now_corr = data_popular_now.corrwith(year['Year'], axis=1)
#print(data_popular_now_corr)
boys_names_popular_now = list(data_popular_now_corr[data_popular_now_corr > 0.8].index)
boys_names_popular_now_data = data[(data['Name'].isin(boys_names_popular_now)) & (data['Year']>=1920) & (data['Gender']=='M')]
boys_names_popular_now_data = boys_names_popular_now_data.pivot(index='Name', columns='Year',values='Count').reset_index().melt('Name', value_name='Count')



#5. 影响美国人取名的因素：体育明星、电视明星#################################
#不知道dodge干嘛的
def name_trend(name, data, gender=['M','F'], year=1920, dodge = 500):
    if isinstance(gender, str):
        name_data = data[(data['Name'] == name)&(data['Gender']==gender)&(data['Year']>=year)]
        attr = list(name_data['Year'].values)
        bar = Bar(name)
        bar.add("", attr, list(name_data['Count'].values), mark_line=["average"], mark_point=["max", "min"],
               legend_text_size=18,xaxis_label_textsize=18,yaxis_label_textsize=18)
        line = Line()
        line.add("", attr, list(name_data['Count'].values + dodge))
        
    else:
        name_data = data[(data['Name'] == name)&(data['Year']>=year)]
        attr = list(range(year, 2018))
        v1 = name_data[name_data['Gender']==gender[0]].Count.values
        v2 = name_data[name_data['Gender']==gender[1]].Count.values
        bar = Bar(name)
        bar.add("男", attr, list(v1), legend_text_size=18,xaxis_label_textsize=18,yaxis_label_textsize=18)
        bar.add("女", attr, list(v2), legend_text_size=18,xaxis_label_textsize=18,yaxis_label_textsize=18)
        line = Line()
        line.add("", attr, list(v1 + dodge))
        line.add("", attr, list(v2 + dodge))
    
    overlap = Overlap()
    overlap.add(bar)
    overlap.add(line)
    return overlap

#name_trend('Jordan',data,gender='M',year=1960).render(r'E:\vscode_code\GitHub项目\interesting_python\English_name\明星.html')


#6. 为什么同一发音的名字，有很多不同的拼写变体？###############################
Catherine = data['Name'][data['Name'].str.contains('^[C|K]ath(.*)')].unique()
#print(Catherine)
Catherine_data = data[data['Name'].isin(Catherine)].groupby('Name').Count.sum()
#print(Catherine_data)
name = list(Catherine_data.index)
value = list(Catherine_data.values)
wordcloud = WordCloud(width=1000, height=600,background_color='#feeeed')  # feeeed
wordcloud.add("", name, value, word_size_range=[20, 100],shape='diamond')
wordcloud


#7. 一些具有特殊含义的名字，有多少人取？(和5一样的套路)
def name_trend2(name, data, gender, dodge=100):
    name_data = data[(data['Name']==name)&(data['Gender']==gender)]
    attr = list(name_data['Year'].values)
    v1 = name_data['Count'].values

    bar = Bar(name)
    bar.add("", attr, list(v1), legend_text_size=18,xaxis_label_textsize=18,yaxis_label_textsize=18)
    
    line = Line()
    line.add("", attr, list(v1 + dodge))
    
    overlap = Overlap()
    overlap.add(bar)
    overlap.add(line)
    return overlap

name_trend2('Dick',data,gender='M', dodge=50)

"""
