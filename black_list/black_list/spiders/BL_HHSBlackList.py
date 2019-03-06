from scrapy import Spider
import os


class BlHhsblacklistSpider(Spider):
    name = 'BL_HHSBlackList'
    allowed_domains = ['oig.hhs.gov']
    start_urls = ['http://oig.hhs.gov/exclusions/downloadables/UPDATED.csv']

    def parse(self, response):
        with open(os.path.abspath('results/HHSBlackList_UPDATED.csv'), 'ab') as f:
            f.write(response.body)
