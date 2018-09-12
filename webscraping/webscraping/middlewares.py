# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ProxyMiddleware(object):
    def __init__(self, proxy_url):
        self.proxy_url = proxy_url

    def process_request(self, request, spider):
        request.meta['proxy'] = self.proxy_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            proxy_url=crawler.settings.get('PROXY_URL')
        )
