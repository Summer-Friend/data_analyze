'''
@Author: your name
@Date: 2020-02-04 13:53:42
@LastEditTime : 2020-02-04 13:57:28
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\盲僧抓包\函数分析.py
'''
lis = list()
print(lis)
#从原型可以看出, append方法接收一个任意类型的对象作为参数行为(功能): 将object直接添加到列表实例对象
lis.append(1)
lis.append([2,3,4])
print(lis)
#从原型可以看出, extend方法接收一个可迭代对象作为参数行为(功能): 将可迭代对象的每一个元素添加到列表实例对象
lis.extend([2,3,4])
lis.extend(range(3))
print(lis)
#从原型可以看出, +运算符接收一个列表实例对象, 并返回一个新的列表实例对象
"""
行为(功能): 行为类似extend方法

与extend的区别:
行为区别: extend改变自身, +运算符不改变自身, 而是返回一个副本(新的实例)
参数区别: extend接收任意可迭代对象作为参数, +运算符仅可接收列表作为参数
"""
lis2 = lis+[5,6,7]
print(lis2)
print(lis)