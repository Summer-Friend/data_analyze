'''
@Author: your name
@Date: 2020-03-05 22:34:40
@LastEditTime: 2020-03-05 22:47:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\盲僧招聘\test.py
'''
import time
import requests
from lxml import etree
import pandas as pd


def sxs_spider(job, pages):
    # 定义函数，爬取通过职位搜索得到的每个职位信息，把爬取的内容保存到本地的csv文件中，参数为：
    # job：搜索的职位
    # pages：爬取的页数（需要根据总共有多少页而定）
    print('Job: {}, '.format(job), 'pages: {}. '.format(str(pages)), 'Challenge accepted!')
    base_url = 'https://www.shixiseng.com/interns?'
    for page in range(1, pages+1):
        url = base_url + 'k=' + job + '&p=' + str(page)
        response = requests.get(url=url)
        time.sleep(2)  # 怕有反爬，每页睡两秒，当然也可以去掉
        decrypted_text = decrypt_text(response.text)  # 爬取回来的原始数据都是经过字体加密的，需要定义一个函数解密
        basic_data = process_text(decrypted_text)  # 定义一个函数处理解密后的文本，返回一个pd.DataFrame格式数据
        print(basic_data)

        print('Successfully crawled page {} and saved it to csv file.'.format(page))


mapping = {'&#xe66f': '0', '&#xe50e': '1', '&#xf19c': '2', '&#xe2d1': '3', '&#xe372': '4',
           '&#xeb5a': '5', '&#xf37c': '6', '&#xf8b6': '7', '&#xf252': '8', '&#xf3a0': '9'}  # 映射字典，使用时需自行更新


def decrypt_text(text):
    # 定义文本信息处理函数，通过字典mapping中的映射关系解密
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text


def process_text(text):
    # 文本处理函数
    parsed_text = etree.HTML(text)
    
    com_links = process_links(parsed_text.xpath('//*[@class="company-box"]/a/@href'))
    # 爬取回来的链接是相对路径，定义一个process_links函数把路径补全
    job_links = process_links(parsed_text.xpath('//*[@class="name-box clearfix"]/a/@href'))
    tag = parsed_text.xpath('//*[@class="company-box"]/span[2]/text()')
    released_time = parsed_text.xpath('//*[@class="name-box clearfix"]/span/text()')
    wage = parsed_text.xpath('//*[@class="more"]/span[1]/text()')
    day_per_week = parsed_text.xpath('//*[@class="more"]/span[2]/text()')
    time_span = parsed_text.xpath('//*[@class="more"]/span[3]/text()')

    data = {'com_links': com_links, 'job_links': job_links, 'tag': tag,
            'released_time': released_time, 'wage': wage, 'day_per_week': day_per_week, 'time_span': time_span
            }

    basic_data = pd.DataFrame.from_dict(data=data)

    return basic_data


def process_links(links):
    # 链接处理函数
    return ['https://www.shixiseng.com' + link for link in links]


def process_list(li):
    # xpath返回的列表处理函数
    if len(li) > 0:
        return li[0]
    else:
        return None



if __name__ == '__main__':
    sxs_spider('算法', 2)
    print('Mission completed!')