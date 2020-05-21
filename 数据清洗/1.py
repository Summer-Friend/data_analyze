'''
@Author: your name
@Date: 2020-02-10 21:44:04
@LastEditTime : 2020-02-13 10:40:27
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\数据清洗\1.py
'''
import pandas as pd
import numpy as np 

"""
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                      'k2': [1, 1, 2, 3, 3, 4, 4]})
#返回一个布尔型Series，表示各行是否是重复行（前面出现过的行）
data.duplicated()

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                               'Pastrami', 'corned beef', 'Bacon',
                               'pastrami', 'honey ham', 'nova lox'],
                      'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
#把他全部转化为小写字母
lowercased = data['food'].str.lower()

meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}
#Series的map方法可以接受一个函数或含有映射关系的字典型对象
#传入对象
data['animal'] = lowercased.map(meat_to_animal)
#传入函数
data['food'].map(lambda x: meat_to_animal[x.lower()])

df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
print(df)
#通过需要排列的轴的长度调用permutation，可产生一个表示新顺序的整数数组：（permuting，随机重排序）
samper = np.random.permutation(5)
print(samper)
#take函数用以获取对应索引的信息
df.take(samper)

#分类，当分类类别数超过总数，可用replace参数
choices = pd.Series([5, 7, -1, 6, 4])
#print(choices.sample(10,replace=True))
draws = choices.sample(n=10, replace=True)
"""

#计算指标/哑变量#########################################
#将分类变量（categorical variable）转换为“哑变量”或“指标矩阵”。
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})
#print(df)
#print(pd.get_dummies(df['key']))

#给指标DataFrame的列加上一个前缀，以便能够跟其他数据进行合并
dummies = pd.get_dummies(df['key'], prefix='key')
#print(dummies)



