# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HurlItem(scrapy.Item):
    # define the fields for your item here like:
     #name = scrapy.Field()
    name=scrapy.Field()

    pass

class YouxiItem(scrapy.Item):
    url=scrapy.Field()
    pass

class ProductItem(scrapy.Item):
    url=scrapy.Field()
    name=scrapy.Field()
    content=scrapy.Field()
    pass
