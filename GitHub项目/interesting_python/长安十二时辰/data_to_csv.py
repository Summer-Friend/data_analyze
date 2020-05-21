'''
@Author: your name
@Date: 2020-02-04 11:40:07
@LastEditTime : 2020-02-04 20:18:37
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\长安十二时辰\data_to_csv.py
'''
import pandas as pd
import matplotlib.pyplot as plt
import pymongo
# 连接mongodb数据库
client = pymongo.MongoClient("localhost")
# 连接数据库
db = client["Changan"]
# 数据表
youku1 = db["youku1"]
#将mongodb中的数据读出
data = pd.DataFrame(list(youku1.find()))
#这里只提取前五行，，这个数据太大了吃不消
data = data.sample(3000)
#print(data['content'])
# 保存为csv格式
data.to_csv(r'E:\vscode_code\GitHub项目\interesting_python\长安十二时辰\Changan.csv',encoding='utf-8')
print('录入成功')
#print(data.columns)
# 找出所有满足字段的行
#df1 = data.loc[:,["content"]]
#print(df1.head())