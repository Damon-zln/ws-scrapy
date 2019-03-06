from bs4 import BeautifulSoup
from black_list.items import BLMoneyLaunderingListItem
from scrapy import Spider
import os


class BlMoneylaunderinglistSpider(Spider):
    name = 'BL_MoneyLaunderingList'
    allowed_domains = ['www.fincen.gov']
    start_urls = ['https://www.fincen.gov/resources/statutes-and-regulations/311-special-measures']
    header = 'NAME|FINDING|NOTICE OF PROPOSED RULEMAKING|FINAL RULE|RESCINDED'

    def parse(self, response):
        with open(os.path.abspath('results/BL_MoneyLaunderingList.txt'), 'a', encoding='utf-8') as f:
            f.write(self.header + '\n')
        soup = BeautifulSoup(response.text, 'lxml')
        trs = soup.select('#special-measures-table tr')
        trs.pop(0)
        trs.pop(-1)
        for tr in trs:
            item = BLMoneyLaunderingListItem()
            item['name'] = tr.select('td:nth-of-type(1)')[0].text.replace('\n', ', ').strip()
            item['finding'] = tr.select('td:nth-of-type(2)')[0].text.replace('\n', ', ').strip()
            item['notice_of_proposed'] = tr.select('td:nth-of-type(3)')[0].text.replace('\n', ', ').strip()
            item['final_rule'] = tr.select('td:nth-of-type(4)')[0].text.strip('\n').replace('\n', ', ').strip()
            item['rescinded'] = tr.select('td:nth-of-type(5)')[0].text.replace('\n', ', ').strip()
            yield item
