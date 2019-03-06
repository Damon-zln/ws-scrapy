# -*- coding: utf-8 -*-


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
