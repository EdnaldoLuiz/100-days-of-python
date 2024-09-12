import scrapy
from scrapy_redis.spiders import RedisSpider

class ExampleSpider(RedisSpider):
    name = 'example'
    redis_key = 'example:start_urls'

    def parse(self, response):
        title = response.xpath('//title/text()').get()
        yield {'title': title}