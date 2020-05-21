'''
@Author: your name
@Date: 2020-03-08 17:47:44
@LastEditTime: 2020-03-08 17:50:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\数据分析第二版\pandas函数\常用函数集.py
'''
#https://blog.csdn.net/zhuxiaodong030/article/details/54316345
#https://blog.csdn.net/liufang0001/article/details/77856255?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
---------------numpy-----------------------
arr = np.array([1,2,3], dtype=np.float64)
np.zeros((3,6))  np.empty((2,3,2)) np.arange(15)
arr.dtype arr.ndim arr.shape
arr.astype(np.int32) #np.float64 np.string_ np.unicode_
arr * arr arr - arr 1/arr
arr= np.arange(32).reshape((8,4))
arr[1:3, : ]  #正常切片
arr[[1,2,3]]  #花式索引
arr.T   arr.transpose((...))   arr.swapaxes(...) #转置
arr.dot #矩阵内积
np.sqrt(arr)   np.exp(arr)    randn(8)＃正态分布值   np.maximum(x,y)
np.where(cond, xarr, yarr)  ＃当cond为真，取xarr,否则取yarr
arr.mean()  arr.mean(axis=1)   #算术平均数
arr.sum()   arr.std()  arr.var()   #和、标准差、方差
arr.min()   arr.max()   #最小值、最大值
arr.argmin()   arr.argmax()    #最小索引、最大索引
arr.cumsum()    arr.cumprod()   #所有元素的累计和、累计积
arr.all()   arr.any()   # 检查数组中是否全为真、部分为真
arr.sort()   arr.sort(1)   #排序、1轴向上排序
arr.unique()   #去重
np.in1d(arr1, arr2)  #arr1的值是否在arr2中
np.load() np.loadtxt() np.save() np.savez() ＃读取、保存文件
np.concatenate([arr, arr], axis=1)  ＃连接两个arr，按行的方向
 
 
---------------pandas-----------------------
ser = Series()     ser = Series([...], index=[...])  #一维数组, 字典可以直接转化为series
ser.values    ser.index    ser.reindex([...], fill_value=0)  #数组的值、数组的索引、重新定义索引
ser.isnull()   pd.isnull(ser)   pd.notnull(ser)   #检测缺失数据
ser.name=       ser.index.name=    #ser本身的名字、ser索引的名字
ser.drop('x') #丢弃索引x对应的值
ser +ser  #算术运算
ser.sort_index()   ser.order()     ＃按索引排序、按值排序
df = DataFrame(data, columns=[...], index=[...]) #表结构的数据结构，既有行索引又有列索引
df.ix['x']  #索引为x的值    对于series，直接使用ser['x']
del df['ly']  #用del删除第ly列
df.T    #转置
df.index.name df.columns.name df.values
df.drop([...])
df + df   df1.add(df2, fill_vaule=0) #算术运算
df -ser   #df与ser的算术运算
f=lambda x: x.max()-x.min()   df.apply(f)
df.sort_index(axis=1, ascending=False)   #按行索引排序
df.sort_index(by=['a','b'])   #按a、b列索引排序
ser.rank()   df.rank(axis=1)  #排序，增设一个排名值
df.sum()   df.sum(axis=1)   #按列、按行求和
df.mean(axis=1, skipna=False)   #求各行的平均值，考虑na的存在
df.idxmax()   #返回最大值的索引
df.cumsum()   #累计求和
df.describe()  ser.describe()   #返回count mean std min max等值
ser.unique()  #去重
ser.value_counts()   df.value_counts()  ＃返回一个series，其索引为唯一值，值为频率
ser.isin(['x', 'y'])  #判断ser的值是否为x,y，得到布尔值
ser.dropna() ser.isnull() ser.notnull() ser.fillna(0)  #处理缺失数据，df相同
df.unstack()   #行列索引和值互换  df.unstack().stack()
df.swaplevel('key1','key2')   #接受两个级别编号或名称，并互换
df.sortlevel(1) #根据级别1进行排序，df的行、列索引可以有两级
df.set_index(['c','d'], drop=False)    #将c、d两列转换为行,因drop为false，在列中仍保留c,d
read_csv   read_table   read_fwf    #读取文件分隔符为逗号、分隔符为制表符('\t')、无分隔符（固定列宽）
pd.read_csv('...', nrows=5) #读取文件前5行
pd.read_csv('...', chunksize=1000) #按块读取，避免过大的文件占用内存
pd.load() #pd也有load方法，用来读取二进制文件
pd.ExcelFile('...xls').parse('Sheet1')  # 读取excel文件中的sheet1
df.to_csv('...csv', sep='|', index=False, header=False) #将数据写入csv文件，以｜为分隔符，默认以，为分隔符, 禁用列、行的标签
pd.merge(df1, df2, on='key', suffixes=('_left', '_right')) #合并两个数据集,类似数据库的inner join, 以二者共有的key列作为键,suffixes将两个key分别命名为key_left、key_right
pd.merge(df1, df2, left_on='lkey', right_on='rkey') #合并，类似数据库的inner join, 但二者没有同样的列名，分别指出，作为合并的参照
pd.merge(df1, df2, how='outer') #合并，但是是outer join；how='left'是笛卡尔积，how='inner'是...;还可以对多个键进行合并
df1.join(df2, on='key', how='outer')  #也是合并
pd.concat([ser1, ser2, ser3], axis=1) #连接三个序列，按行的方向
ser1.combine_first(ser2)   df1.combine_first(df2) #把2合并到1上，并对齐
df.stack() df.unstack()  #列旋转为行、行旋转为列
df.pivot()
df.duplicated()   df.drop_duplicates() #判断是否为重复数据、删除重复数据
df[''].map(lambda x: abs(x)) #将函数映射到df的指定列
ser.replace(-999, np.nan) #将－999全部替换为nan
df.rename(index={}, columns={}, inplace=True) #修改索引，inplace为真表示就地修改数据集
pd.cut(ser, bins)  #根据面元bin判断ser的各个数据属于哪一个区段，有labels、levels属性
df[(np.abs(df)>3).any(1)] #输出含有“超过3或－3的值”的行
permutation  take    #用来进行随机重排序
pd.get_dummies(df['key'], prefix='key')  #给df的所有列索引加前缀key
df[...].str.contains()  df[...].str.findall(pattern, flags=re.IGNORECASE)  df[...].str.match(pattern, flags=...)    df[...].str.get()  #矢量化的字符串函数
 
----绘图
ser.plot() df.plot() #pandas的绘图工具，有参数label, ax, style, alpha, kind, logy, use_index, rot, xticks, xlim, grid等，详见page257
kind='kde' #密度图
kind='bar' kind='barh' #垂直柱状图、水平柱状图，stacked=True为堆积图
ser.hist(bins=50) #直方图
plt.scatter(x,y) #绘制x,y组成的散点图
pd.scatter_matrix(df, diagonal='kde', color='k', alpha='0.3')  #将df各列分别组合绘制散点图
 
----聚合分组
groupby() 默认在axis=0轴上分组，也可以在1组上分组；可以用for进行分组迭代
df.groupby(df['key1']) #根据key1对df进行分组
df['key2'].groupby(df['key1'])  #根据key1对key2列进行分组
df['key3'].groupby(df['key1'], df['key2'])  #先根据key1、再根据key2对key3列进行分组
df['key2'].groupby(df['key1']).size() #size()返回一个含有分组大小的series
df.groupby(df['key1'])['data1']  等价于 df['data1'].groupby(df['key1'])
df.groupby(df['key1'])[['data1']]  等价于  df[['data1']].groupby(df['key1'])
df.groupby(mapping, axis=1)  ser(mapping) #定义mapping字典，根据字典的分组来进行分组
df.groupby(len) #通过函数来进行分组，如根据len函数
df.groupby(level='...', axis=1)  #根据索引级别来分组
df.groupby([], as_index=False)   #禁用索引，返回无索引形式的数据
df.groupby(...).agg(['mean', 'std'])   #一次使用多个聚合函数时，用agg方法
df.groupby(...).transform(np.mean)   #transform()可以将其内的函数用于各个分组
df.groupby().apply()  #apply方法会将待处理的对象拆分成多个片段，然后对各片段调用传入的函数，最后尝试将各片段组合到一起
 
----透视交叉
df.pivot_table(['',''], rows=['',''], cols='', margins=True)  #margins为真时会加一列all
pd.crosstab(df.col1, df.col2, margins=True) #margins作用同上
 
 
---------------matplotlib---------------
fig=plt.figure() ＃图像所在的基对象
ax=fig.add_subplot(2,2,1)  #2*2的图像，当前选中第1个
fig, axes = plt.subplots(nrows, nclos, sharex, sharey)  #创建图像，指定行、列、共享x轴刻度、共享y轴刻度
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
#调整subplot之间的距离，wspace、hspace用来控制宽度、高度百分比
ax.plot(x, y, linestyle='--', color='g')   #依据x,y坐标画图，设置线型、颜色
ax.set_xticks([...]) ax.set_xticklabels([...]) #设置x轴刻度
ax.set_xlabel('...') #设置x轴名称
ax.set_title('....') ＃设置图名
ax.legend(loc='best') #设置图例， loc指定将图例放在合适的位置
ax.text(x,y, 'hello', family='monospace', fontsize=10) #将注释hello放在x,y处，字体大小为10
ax.add_patch() #在图中添加块
plt.savefig('...png', dpi=400, bbox_inches='tight') #保存图片，dpi为分辨率，bbox＝tight表示将裁减空白部分
 
 
 
 
------------------------------------------
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#可以用来绘制地图
 
 
-----------------时间序列--------------------------
pd.to_datetime(datestrs)    #将字符串型日期解析为日期格式
pd.date_range('1/1/2000', periods=1000)    #生成时间序列
ts.resample('D', how='mean')   #采样，将时间序列转换成以每天为固定频率的, 并计算均值；how='ohlc'是股票四个指数；
＃重采样会聚合，即将短频率（日）变成长频率（月），对应的值叠加；
＃升采样会插值，即将长频率变为短频率，中间产生新值
ts.shift(2, freq='D')   ts.shift(-2, freq='D') #后移、前移2天
now+Day() now+MonthEnd()
import pytz   pytz.timezone('US/Eastern')   #时区操作，需要安装pytz
pd.Period('2010', freq='A-DEC')   ＃period表示时间区间，叫做时期
pd.PeriodIndex    #时期索引
ts.to_period('M')   #时间转换为时期
pd.rolling_mean(...)    pd.rolling_std(...)   #移动窗口函数－平均值、标准差
