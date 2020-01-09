# 将数据导出的语法
# scrapy crawl quotes -o quotes.csv
# scrapy crawl quotes -o quotes.xml
# scrapy crawl quotes -o quotes.pickle
# scrapy crawl quotes -o quotes.marshal
import scrapy
# 引入定义的item
from scrapyTest.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
          # 将爬取到的数据存入item
          item = QuoteItem()
          item['text'] = quote.css('.text::text').extract_first()
          item['author'] = quote.css('.author::text').extract_first()
          item['tags'] = quote.css('.tags .tag::text').extract_first()
          yield item
        next = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url= url, callback= self.parse)
