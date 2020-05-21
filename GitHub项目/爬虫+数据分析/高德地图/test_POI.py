'''
@Author: your name
@Date: 2020-02-02 11:52:34
@LastEditTime : 2020-02-02 11:54:55
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\爬虫+数据分析\高德地图\test_POI.py
'''
import requests
import json
import pprint
url = 'https://restapi.amap.com/v3/place/text?types=050000&city=长沙&offset=20&page=1&key=这是你的key'

res = requests.get(url)
#print(res.text)
result = json.loads(res.text)
pprint.pprint(result)
'''
count = result['count']
print(count)
'''