# -*- coding: utf-8 -*-

from scrapy import Item, Field


class CommentItem(Item):
    collection = 'comm_id'
    id = Field()
    weibo_id = Field()
