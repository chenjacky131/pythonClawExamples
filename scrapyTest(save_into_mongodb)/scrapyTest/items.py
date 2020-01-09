import scrapy


class QuoteItem(scrapy.Item):
    # 创建item需要继承scrapy.Item类
    # 并且定义类型为Field的字段
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    pass
