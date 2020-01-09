# -*- coding: utf-8 -*-
# 管道的作用：
# 清洗 HTML 数据
# 验证爬取数据，检查爬取字段
# 查重并丢弃重复内容
# 将爬取结果储存到数据库
from scrapy.exceptions import DropItem
import pymongo

class TextPipeline(object):
    def process_item(self, item, spider):
        if item['text']:
          return item
        else:
          return DropItem('Missing Text')

class MongoPipeline(object):
  def __init__(self, mongo_uri, mongo_db):
    self.mongo_uri = mongo_uri
    self.mongo_db = mongo_db
  
  @classmethod
  def from_crawler(cls, crawler):
    return cls(mongo_uri=crawler.settings.get('MONGO_URI'),
              mongo_db=crawler.settings.get('MONGO_DB')
    )
  
  def open_spider(self, spider):
    self.client = pymongo.MongoClient(self.mongo_uri)
    self.db = self.client[self.mongo_db]
  
  def process_item(self, item, spider):
    name = item.__class__.__name__
    self.db[name].insert(dict(item))
    return item
  
  def close_spider(self, spider):
    self.client.close()