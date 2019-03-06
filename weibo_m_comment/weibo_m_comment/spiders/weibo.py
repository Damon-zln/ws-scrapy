from scrapy import Request, Spider
from weibo_m_comment.items import *
import json
import pymongo
from weibo_m_comment.settings import *


class WeiziSpider(Spider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']
    # 评论
    comment_url = 'https://m.weibo.cn/comments/hotflow?id={uid}&mid={uid}'
    comment_url2 = 'https://m.weibo.cn/comments/hotflow?id={uid}&mid={uid}&max_id={max_id}'
    # 微博ID集合
    client = pymongo.MongoClient(MONGO_URI, 27017)
    db = client[MONGO_DB]
    table = db['weibos']
    weibo_m = [str(i["id"]) for i in table.find({"text": {"$regex": KEY_WORD, "$options": "i"}}).limit(LIMIT)]

    def start_requests(self):
        for wei_id in self.weibo_m:
            yield Request(self.comment_url.format(uid=wei_id), callback=self.parse_comment, meta={'uid': wei_id})

    def parse_comment(self, response):
        result = json.loads(response.text)
        if result.get('ok') == 1 and result.get('data').get('data'):
            comms = result.get('data').get('data')
            for comm in comms:
                user = comm.get('user')
                if user:
                    comm_item = CommentItem()
                    comm_item['id'] = user.get('id')
                    comm_item['weibo_id'] = response.meta.get('uid')
                    yield comm_item
            # 下一页微博
            wei_id = response.meta.get('uid')
            max_id = result.get('data').get('max_id')
            if max_id:
                yield Request(self.comment_url2.format(uid=wei_id, max_id=max_id), callback=self.parse_comment, meta={'max_id': max_id, 'uid': wei_id})
