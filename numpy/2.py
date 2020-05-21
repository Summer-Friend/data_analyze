'''
@Author: your name
@Date: 2020-03-27 21:40:10
@LastEditTime: 2020-03-27 21:50:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\数据分析第二版\numpy\2.py
'''
import numpy as np  
from io import BytesIO

a = np.arange(10)**3
a[:6:2] = -1000    # equivalent from start to position 6, exclusive, set every 2nd element to -1000
b = np.arange(12).reshape(4,3)    

'''
在这里，python3和Python2在套接字返回值解码上有区别。
需要用上python的bytes和str两种类型转换的函数encode()、decode()
'''
data = "1, 2, 3\n4, 5, 6"
c = np.genfromtxt(BytesIO(data.encode()), delimiter=",")
print(c)
