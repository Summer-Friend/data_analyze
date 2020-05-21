'''
@Author: your name
@Date: 2020-02-04 13:59:05
@LastEditTime: 2020-02-04 13:59:21
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\盲僧抓包\json解码fenxi.py
'''
import json
  
data = {
  "statusCode": 200,
  "data": {
    "totoal": "5",
    "height": "5.97",
    "weight": "10.30",
    "age": "11"
  },
  "msg": "成功"
}
  
#dumps:把字典转换为json字符串
s = json.dumps(data)
print(s)
  
#loads:把json转换为dict
ss = json.loads(s)
print(ss)
 
#打印msg对应的值print(s["msg"]) #TypeError: string indices must be integers
print(ss["msg"])
 
#打印data下age对应的值
print(ss["data"]["age"])