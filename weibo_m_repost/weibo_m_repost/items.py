# -*- coding: utf-8 -*-

from scrapy import Item, Field


class RepostItem(Item):
    collection = 'repost_id'
    id = Field()
    weibo_id = Field()
