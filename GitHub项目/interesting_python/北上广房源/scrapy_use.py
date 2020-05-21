'''
@Author: your name
@Date: 2020-02-02 17:00:01
@LastEditTime: 2020-02-02 17:00:04
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\interesting_python\北上广房源\scrapy_use.py
'''
 1 import scrapy
 2 
 3 
 4 class huyalol(scrapy.Spider):
 5     name = "huyalol"
 6     start_urls = ["https://www.huya.com/g/lol"]
 7 
 8     def parse(self, response):
 9         title_list = response.xpath('//*[@id="js-live-list"]/li/a[2]/text()').extract()
10         name_list = response.xpath('//*[@id="js-live-list"]/li/span/span[1]/i/text()').extract()
11         for i in range(1,11):
12             print(name_list[i-1], ': ',title_list[i-1])