'''
@Author: your name
@Date: 2020-02-02 11:39:06
@LastEditTime : 2020-02-02 11:50:34
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\爬虫+数据分析\简书\data_get.py
'''
import requests

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

url = 'http://e.hiphotos.baidu.com/image/pic/item/83025aafa40f4bfb0f815ad60e4f78f0f63618db.jpg'

res = requests.get(url,headers=headers)
fp = open('1.jpg','wb')
fp.write(res.content)
fp.close()

