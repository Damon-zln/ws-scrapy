from scrapy import Request, Spider
from weibo_m_repost.items import *
import json
import pymongo
from weibo_m_repost.settings import MONGO_DB, MONGO_URI, LIMIT, KEY_WORD


class WeiziSpider(Spider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']
    # 转发
    repost_url = 'https://m.weibo.cn/api/statuses/repostTimeline?id={uid}&page={page}'
    # 微博ID集合
    client = pymongo.MongoClient(MONGO_URI, 27017)
    db = client[MONGO_DB]
    table = db['weibos']
    weibo_m = [str(i["id"]) for i in table.find({"text": {"$regex": KEY_WORD, "$options": "i"}}).limit(LIMIT)]

    def start_requests(self):
        for wei_id in self.weibo_m:
            yield Request(self.repost_url.format(uid=wei_id, page=1), callback=self.parse_repost, meta={'page': 1, 'uid': wei_id})

    def parse_repost(self, response):
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('data'):
            reposts = result.get('data').get('data')
            for repost in reposts:
                user = repost.get('user')
                if user:
                    repost_item = RepostItem()
                    repost_item['id'] = user.get('id')
                    repost_item['weibo_id'] = response.meta.get('uid')
                    yield repost_item
            # 下一页转发
            wei_id = response.meta.get('uid')
            page = response.meta.get('page') + 1
            yield Request(self.repost_url.format(uid=wei_id, page=page), callback=self.parse_repost, meta={'page': page, 'uid': wei_id})