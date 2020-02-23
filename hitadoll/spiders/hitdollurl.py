# -*- coding: utf-8 -*-
import scrapy
import pdb

import simplejson as simplejson
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hitadoll.classes.articles import Articles
import logging
import json

from hitadoll.items import ProductItem


class HitdollurlSpider(CrawlSpider):
    name = 'hitdollurl'
    allowed_domains = ['www.hitdoll.com']
    start_urls = [#'http://www.hitdoll.com/yzxl/list_645.aspx',
                  'http://www.hitdoll.com/omxl/list_646.aspx',
                  'http://www.hitdoll.com/znww/list_647.aspx'
                  ]

    rules = (
        Rule(LinkExtractor(allow=r'\/yzxl\/info_645\.aspx\?itemid=\d+',deny=('cid=')), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'\/omxl\/info_646\.aspx\?itemid=\d+',deny=('cid=')), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'\/znww\/info_647\.aspx\?itemid=\d+',deny=('cid=')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        """

        :type response: object
        """
        articles=Articles()
        result =articles.verify(response.url)
        logging.warning('result is %s' % result)
        objresult = simplejson.loads(result)
        #logging.warning('item is %s'%objresult['status'])

        if(objresult['status']):
            i = ProductItem()
            i['url']=response.url
            i['name']=response.xpath('//h1/text()').extract()
            logging.warning("item name %s"%i['name'])
            i['content'] = response.xpath('//div[@class="SinglePage"]/node()').extract()
            #yield
            #logging.warning("This is content %s" % i['content'])
            #i['name'] = response.xpath('//div[@id="name"]').extract()
            #i['description'] = response.xpath('//div[@id="description"]').extract()
            return i
