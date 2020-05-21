'''
@Author: your name
@Date: 2020-02-04 20:19:19
@LastEditTime : 2020-02-06 16:13:24
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\长安十二时辰\数据分析.py
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import Polar


data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\长安十二时辰\Changan.csv')

#print(data['content'].head())

# createTime字段
data['bj_time'] = pd.to_datetime(data['createTime'].values, unit='ms', utc=True).tz_convert('Asia/Shanghai')
data['emoji'] = data['content'].str.extract("\[(.*?)\]")
#print(data['emoji'].head())

#value_counts是一种查看表格某列中有多少个不同值的快捷方法，并计算每个不同值有在该列中个数
emoji = data['emoji'].value_counts()[:15]
#极坐标图
polar = Polar(" ", width=1200, height=600)
polar.add(
    "",
    emoji.values,
    angle_data=emoji.index,
    type="barAngle",
    is_stack=True,
)

polar.render(r'E:\vscode_code\GitHub项目\interesting_python\长安十二时辰\情感分析.html')

