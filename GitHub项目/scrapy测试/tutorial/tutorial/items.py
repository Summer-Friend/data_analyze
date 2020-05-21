'''
@Author: your name
@Date: 2020-02-02 17:12:34
@LastEditTime: 2020-02-02 19:53:38
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \vscode_code\GitHub项目\scrapy测试\tutorial\tutorial\items.py
'''
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DoubanMovieItem(scrapy.Item):
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()
