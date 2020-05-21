'''
@Author: your name
@Date: 2020-02-12 10:58:20
@LastEditTime: 2020-02-17 15:00:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\其他\数据分析第二版\numpy\1.py
'''
import numpy as np

my_arr = np.arange(10)
#print((my_arr)[1])
my_list = list(range(10))
#print(my_list[1])

arr = np.arange(8)
#1.数组重塑###################################################
arr2 = arr.reshape(4,2)
#reshape将一维数组转换为多维数组的运算过程相反的运算通常称为扁平化（flattening）或散开（raveling）：
arr3 = arr2.ravel()
arr4 = arr2.flatten()
#print(arr3, arr4)

#2.数据的合并和拆分#############################################3
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
#按列合并
np.concatenate([arr1, arr2], axis=0)
#按行合并
np.concatenate([arr1, arr2], axis=1)

#对于常见的连接操作，NumPy提供了一些比较方便的方法（如vstack和hstack）
#按列合并
np.vstack((arr1, arr2))
#按行合并 
np.hstack((arr1, arr2))

#与此相反，split用于将一个数组沿指定轴拆分为多个数组：传入到np.split的值[1,3]指示在哪个索引处分割数组。
arr = np.random.randn(5, 2)
first, second, third = np.split(arr, [1,3])

#3.元素的重复操作：tile和repeat######################################
arr = np.arange(3)
arr.repeat(3)
#如果传入的是一组整数，则各元素就可以重复不同的次数：但是个数也必须对应
#同样，在对多维进行重复时，也可以传入一组整数，这样就会使各切片重复不同的次数：
arr.repeat([2, 3, 4])
#对于多维数组，还可以让它们的元素沿指定轴重复：
arr = np.random.randn(2, 2)
arr.repeat(2, axis = 1)
#注意，如果没有设置轴向，则数组会被扁平化，这可能不会是你想要的结果
#print(arr.repeat(2))


#4.索引：################################################
# 获取和设置数组子集的一个办法是通过整数数组使用花式索引：
arr = np.arange(10) * 100
inds = [7, 1, 2, 6]
#两种方法一样
arr[inds]
arr.take(inds)
#在inds索引处的数用42代替
arr.put(inds, 42)

#要在其它轴上使用take，只需传入axis关键字即可：
arr = np.random.randn(2, 4)
print(arr)
#抽取arr按行的每个数据的第1,2个
print(arr.take([0, 1], axis =1))


