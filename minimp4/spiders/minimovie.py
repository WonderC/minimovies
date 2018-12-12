# -*- coding: utf-8 -*-
import scrapy
from minimp4.items import Minimp4Item
from lxml import etree

class MinimovieSpider(scrapy.Spider):
    name = 'minimovie'
    allowed_domains = ['www.minimp4.com']
    start_urls = ['http://www.minimp4.com/movie/?page={}'.format(page) for page in range(1,6)]

    def parse(self, response):
        # extract提取文本 列表
        hrefs = response.xpath('//div[@class="meta"]/h1/a/@href').extract()
        for url in hrefs:
            # 生成器
            yield scrapy.Request(url, callback=self.parseContent)

    def parseContent(self, response):
        # name
        name = response.xpath('//div[@class="movie-meta"]/h1/text()').extract()
        # 实例化
        item = Minimp4Item()
        # 字典
        item['name'] = name
        # 返回item
        yield item
