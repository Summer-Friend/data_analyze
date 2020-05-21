'''
@Author: your name
@Date: 2020-03-28 21:14:15
@LastEditTime: 2020-03-29 11:13:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\双色球\大文件读取.py
'''
import pandas as pd 

def knn():
    frame = pd.DataFrame()
    # 读取数据
    file_path = r'E:\vscode_code\多线程\双色球\qiu2.csv'
    
    #https://blog.csdn.net/zm714981790/article/details/51375475
    #https://www.cnblogs.com/shuaishuaidefeizhu/p/9817872.html
    reader = pd.read_csv(file_path, chunksize=20)    # 每块为20条数据(index)
    
    for chunk in reader:
        frame = frame.append(chunk).reset_index(drop=True)
        #print(chunk.head())
        #只输出一块，把这个去掉就是所有数据了
        #break
    print(frame.describe())

 
if __name__ == '__main__':
    knn()