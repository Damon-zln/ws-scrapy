from bs4 import BeautifulSoup
from black_list.items import BLUSForeignTerroristOrgItem
from scrapy import Spider
import os


class BlUsForeignTerroristOrgSpider(Spider):
    name = 'BL_US_Foreign_Terrorist_Org'
    allowed_domains = ['www.state.gov']
    start_urls = ['http://www.state.gov/j/ct/rls/other/des/123085.htm']
    header = 'DateDesignated|DesignatedOrganization|DateRemoved|DelistedOrganization|DateOrginallyDesignated'

    def parse(self, response):
        with open(os.path.abspath('results/BL_US_Foreign_Terrorist_Org.txt'), 'a', encoding='utf-8') as f:
            f.write(self.header + '\n')
        soup = BeautifulSoup(response.text, 'lxml')
        trs1 = soup.select('table:nth-of-type(1) tr')
        trs2 = soup.select('table:nth-of-type(2) tr')
        trs1.pop(0)
        trs2.pop(0)
        trs1.pop(0)
        trs2.pop(0)
        for tr in trs1:
            item = BLUSForeignTerroristOrgItem()
            item['date_designated'] = tr.find_all(name='td')[0].text.strip()
            item['designated_organization'] = tr.find_all(name='td')[1].text.strip()
            item['date_removed'] = ''
            item['delisted_organization'] = ''
            item['date_originally_designated'] = ''
            yield item
        for tr in trs2:
            item = BLUSForeignTerroristOrgItem()
            item['date_designated'] = ''
            item['designated_organization'] = ''
            item['date_removed'] = tr.find_all(name='td')[0].text.strip()
            item['delisted_organization'] = tr.find_all(name='td')[1].text.strip()
            item['date_originally_designated'] = tr.find_all(name='td')[2].text.strip()
            yield item
