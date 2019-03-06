from scrapy import Spider
import os


class BlOfacblockedblacklistSpider(Spider):
    name = 'BL_OFACBlockedBlackList'
    allowed_domains = ['www.treasury.gov']
    start_urls = ['https://www.treasury.gov/ofac/downloads/sdnlist.txt',
                  'https://www.treasury.gov/ofac/downloads/prgrmlst.txt',
                  'https://www.treasury.gov/ofac/downloads/ctrylst.txt']

    def parse(self, response):
        if response.url == 'https://www.treasury.gov/ofac/downloads/sdnlist.txt':
            with open(os.path.abspath('results/OFAC_Blocked_Countries_Complete_Specially_Designated_Nationals_List.txt'), 'ab') as f:
                f.write(response.body)
        if response.url == 'https://www.treasury.gov/ofac/downloads/prgrmlst.txt':
            with open(os.path.abspath('results/OFAC_Blocked_Countries_SDN_List_Sorted_by_OFAC_Sanctions_Program.txt'), 'ab') as f:
                f.write(response.body)
        if response.url == 'https://www.treasury.gov/ofac/downloads/ctrylst.txt':
            with open(os.path.abspath('results/OFAC_Blocked_Countries_SDN_List_Sorted_by_Country.txt'), 'ab') as f:
                f.write(response.body)
