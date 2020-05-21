'''
@Author: your name
@Date: 2020-01-31 10:51:21
@LastEditTime : 2020-01-31 15:08:34
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\数据可视化\pyecharts可视化\keshihua.py
'''
import pandas as pd
import numpy as np
from pyecharts import Pie

data = pd.read_csv(r'E:\vscode_code\GitHub项目\interesting_python\数据可视化\pyecharts可视化\friend.csv',encoding='utf-8')
#print(data.head())
#分组形成一个字典
#sex = data.groupby('Sex')
sex = data.groupby('Sex')['Sex'].count()
#形成一个列表
print(list(sex))
'''
pie = Pie("男女分布", title_pos='center')
pie.add(
    "",
    ['外星人','男性','女性'],
    list(sex),
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
pie.render("sex.html")
'''
#new_data = data[data['Signature'].notnull()]
new_data = data[data['Signature'].notnull()]
print(new_data.head())
#print(data[data['Signature']])