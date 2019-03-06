from scrapy import Request, Spider
from weibo_m.items import *
import json
from weibo_m.settings import START_USER


class WeiziSpider(Spider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']
    # 博主详情API
    user_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=100505{uid}'
    # 微博列表API
    weibo_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&containerid=107603{uid}&page={page}'

    start_users = START_USER

    def start_requests(self):
        for uid in self.start_users:
            yield Request(self.user_url.format(uid=uid), callback=self.parse)

    def parse(self, response):
        """
        解析
        :param response: Response对象
        """
        # self.logger.debug(response)
        result = json.loads(response.text)
        if result.get('data').get('userInfo'):
            user_info = result.get('data').get('userInfo')
            user_item = UserItem()
            field_map = {
                'id': 'id', 'name': 'screen_name', 'avatar': 'profile_image_url', 'cover': 'cover_image_phone',
                'gender': 'gender', 'description': 'description', 'fans_count': 'followers_count', 'follows_count': 'follow_count',
                'weibo_count': 'statuses_count', 'verified': 'verified', 'verified_reason': 'verified_reason',
                'verified_type': 'verified_type'
            }
            for field, attr in field_map.items():
                user_item[field] = user_info.get(attr)
            yield user_item
            uid = user_info.get('id')
            yield Request(self.weibo_url.format(uid=uid, page=1), callback=self.parse_weibo, meta={'page': 1, 'uid': uid})

    def parse_weibo(self, response):
        """
        解析微博列表
        :param response: Response对象
        """
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards'):
            weibos = result.get('data').get('cards')
            for weibo in weibos:
                mblog = weibo.get('mblog')
                if mblog:
                    weibo_item = WeiboItem()
                    field_map = {
                        'id': 'id', 'text': 'text', 'attitudes_count': 'attitudes_count', 'comments_count': 'comments_count',
                        'reposts_count': 'reposts_count', 'created_at': 'created_at'
                    }
                    for field, attr in field_map.items():
                        weibo_item[field] = mblog.get(attr)
                    yield weibo_item
            # 下一页微博
            uid = response.meta.get('uid')
            page = response.meta.get('page') + 1
            yield Request(self.weibo_url.format(uid=uid, page=page), callback=self.parse_weibo,
                          meta={'page': page, 'uid': uid})
