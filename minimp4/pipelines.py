# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class Minimp4Pipeline(object):

    def __init__(self):
        self.f = open('minimovies.json','a','utf-8')
        pass

    # 保存数据
    def process_item(self, item, spider):
        data = json.dumps(dict(item),ensure_ascii=false,encoding='utf-8') +'\n'
        self.f.write(data)
        return item

    def close_spider(self,spider):
        self.f.close()
