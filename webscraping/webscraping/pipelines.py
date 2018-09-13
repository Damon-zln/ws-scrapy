# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from webscraping.items import *


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        if isinstance(item, CA_EngineerItem) or isinstance(item, CA_Prolic_registered_pharmacistItem) \
                or isinstance(item, CA_Prolic_pharmacy_technician) or isinstance(item, CA_Prolic_automotiveItem)\
                or isinstance(item, CA_RealestateItem) or isinstance(item, CA_Prolic_accountancyItem)\
                or isinstance(item, CA_Prolic_acupunctureItem) or isinstance(item, CA_Prolic_architectItem)\
                or isinstance(item, CA_Prolic_courtReporterItem) or isinstance(item, CA_Prolic_hearing_aid_dispenserItem)\
                or isinstance(item, CA_Prolic_professional_fiduciaryItem):
            self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
