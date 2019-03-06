# -*- coding: utf-8 -*-

from scrapy import Item, Field


class UserItem(Item):
    collection = 'user'
    id = Field()
    name = Field()
    avatar = Field()
    cover = Field()
    gender = Field()
    description = Field()
    fans_count = Field()
    follows_count = Field()
    weibo_count = Field()
    verified = Field()
    verified_reason = Field()
    verified_type = Field()
    crawled_at = Field()


class WeiboItem(Item):
    collection = 'weibos'
    id = Field()
    text = Field()
    attitudes_count = Field()
    comments_count = Field()
    reposts_count = Field()
    created_at = Field()
    crawled_at = Field()
