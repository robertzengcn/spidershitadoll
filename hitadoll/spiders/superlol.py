# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SuperlolSpider(CrawlSpider):
    name = 'superlol'
    allowed_domains = ['lol.17173.com']
    start_urls = ['http://lol.17173.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http:\/\/lol\.17173.com\/news\/\d+\/\d+\.shtml'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
