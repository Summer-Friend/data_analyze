'''
@Author: your name
@Date: 2020-02-02 17:20:02
@LastEditTime : 2020-02-02 19:31:09
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\scrapy测试\tutorial\tutorial\spiders\dmoz_spider.py
'''
from scrapy.spiders import Spider


class BlogSpider(Spider):
    name = 'woodenrobot'
    start_urls = ['https://woodenrobot.me']
    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print (title.strip())