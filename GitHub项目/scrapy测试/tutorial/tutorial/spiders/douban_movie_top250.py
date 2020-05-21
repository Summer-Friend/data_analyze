'''
@Author: your name
@Date: 2020-02-02 19:54:18
@LastEditTime : 2020-02-02 21:40:14
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\scrapy测试\tutorial\tutorial\spiders\douban_movie_top250.py
'''
from scrapy import Request
from scrapy.spiders import Spider
from tutorial.items import DoubanMovieItem
class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        for i in range(10):
            url = 'https://movie.douban.com/top250?start={}'.format(i*10)
            yield Request(url, headers=self.headers)
    def parse(self, response):
        item = DoubanMovieItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            #这个玩意儿用xpath的copy xpath一样的效果
            #不加extract时，返回一个SelectorList 对象；使用extract() ，返回一个列表，里面是提取的内容
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            yield item
          