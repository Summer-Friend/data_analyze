'''
@Author: your name
@Date: 2020-03-01 20:07:11
@LastEditTime: 2020-03-01 20:09:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\数据分析第二版\pandas\map_apply.py
'''
import pandas as pd 
'''
apply 用在dataframe上，用于对row或者column进行计算；

applymap 用于dataframe上，是元素级别的操作；

map （其实是python自带的）用于series上，是元素级别的操作。
'''
df = pd.DataFrame(np.random.randint(0,10,(4, 3)), columns=list('bde'), index=range(4))
f = lambda x: x.max() - x.min()
df.apply(f) 
df.apply(f,axis=1)  # 作用在一行上
df.apply(f,axis=0)  # 作用在一列上，axis=0可省略

#applymap： 作用在dataframe的每一个元素上
f2 = lambda x: x+1 if x%2==0 else x
df.applymap(f2)