from scrapy import Spider, Request
import os


class BlofacsdnblacklistSpider(Spider):
    name = 'BL_OFACSDNBlackList'
    allowed_domains = ['www.treasury.gov']
    start_urls = ['https://www.treasury.gov/resource-center/sanctions/SDN-List/Documents/dat_spec.txt']

    def parse(self, response):
        with open(os.path.abspath('results/OFAC_SDN_Layout.txt'), 'a') as f:
            f.write(response.text)
        yield Request('https://www.treasury.gov/ofac/downloads/sdall.zip', callback=self.parse2)

    def parse2(self, response):
        with open(os.path.abspath('results/OFAC_SDN_sdall.zip'), 'wb') as f:
            f.write(response.body)
