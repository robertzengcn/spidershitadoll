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


class ActionSpider(CrawlSpider):
    name = 'action'
    allowed_domains = ['play.mob.org']
    start_urls = ['http://play.mob.org/genre/brodilki_action/'
                  ]

    rules = (
        Rule(LinkExtractor(allow=r'http:\/\/play\.mob\.org\/genre\/brodilki_action\/page-\d+/'), callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        """

        :type response: object
        """
        articles=Articles()
        result =articles.verify(response.url)
        logging.warning('result is %s' % result)
        objresult = simplejson.loads(result)
        logging.warning('item is %s'%objresult['status'])


