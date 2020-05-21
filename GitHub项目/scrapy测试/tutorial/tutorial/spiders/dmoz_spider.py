'''
@Author: your name
@Date: 2020-02-02 19:32:58
@LastEditTime : 2020-02-02 19:45:16
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\scrapy测试\tutorial\tutorial\spiders\dmoz_spider.py
'''
import scrapy

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print (title, link, desc)
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)