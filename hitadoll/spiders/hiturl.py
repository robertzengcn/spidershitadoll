#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
import logging
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


from hitadoll.items import HurlItem


class Hiturl(scrapy.spiders.Spider):
    name = "hiturl"
    allowed_domains = ["hitdoll.com"]
    start_urls = [
        "http://www.hitdoll.com/yzxl/list_645.aspx",
    ]

    rules = (
        Rule(LinkExtractor(allow=('.aspx')),
            callback='urlparse', follow=True,
        ),
    )

    def parse(self, response):
        logging.warning("This is url: %s" % response.url)
        pass

    def urlparse(self,response):
        logging.warning("1111111111111111111111111111111111111111111111111111111111111111111111")
        logging.warning("find url: %s" % response.url)
        item=HurlItem();
        item['url']=response.url;
        yield item
        pass



