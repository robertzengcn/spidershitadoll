# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['lol.17173.com']
    start_urls = ['http://lol.17173.com/']
    rules =(
        Rule(LinkExtractor(allow='http:\/\/lol\.17173.com\/news\/\d+\/\d+\.shtml'), callback='parse_items',
             follow=True),
    )



    def parse(self, response):
        self.log('now at url: %s' % response.url);
        pass

    def parse_items(self,response):
        self.log('url: %s'% response.url);
        pass
