# -*- coding: utf-8 -*-
from hitadoll.classes.baitrans import Baitrans
from hitadoll.classes.articles import Articles
from hitadoll.classes.fixurl import Fixurl

try:
    from urlparse import urljoin  # Python2
except ImportError:
    from urllib.parse import urljoin  # Python3

import logging


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HitadollPipeline(object):
    def process_item(self, item, spider):
        baitran= Baitrans()
        #logging.warning("name is %s"%item['name'][0].encode('utf-8'));
        #logging.warning("content is %s"%item['content'][0].encode('utf-8'));
        #[x.encode('utf-8') for x in item['content'][0]]
        contents =''
        contents =contents.join(item['content'])
        fixurl=Fixurl()
        contents=fixurl.fixpath(contents.encode('utf-8'),'http://www.hitdoll.com')

        #logging.warning('contents is %s'%contents.encode('utf-8'));
        itemnames=baitran.tran(item['name'][0].encode('utf-8'), 'zh', 'en')
        #itemcontent=baitran.tran(contents.encode('utf-8'),'zh','en')
        articles=Articles()
        articles.savearticle(itemnames,contents,'sex doll',item['url'])

        return item


