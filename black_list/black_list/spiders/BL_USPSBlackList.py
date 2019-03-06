from scrapy import Spider, Request
from bs4 import BeautifulSoup
from black_list.items import BlUspsblacklistItem
import os


class BluspsblacklisSpider(Spider):
    name = 'BL_USPSBlackList'
    allowed_domains = ['postalinspectors.uspis.gov']
    start_urls = ['https://postalinspectors.uspis.gov/pressroom/wanted.aspx']
    header = 'Title|Violations|CaseNo|NcicNo|FbiNo|WarrantNo|Aliases|Dob|Description|Miscinfo'

    def parse(self, response):
        with open(os.path.abspath('results/BL_USPSBlackList.txt'), 'a', encoding='utf-8') as f:
            f.write(self.header + '\n')
        soup = BeautifulSoup(response.text, 'lxml')
        urls = soup.select('#ctl00_mainContent_RadEditor1 tr > td a')
        baseUrl = 'https://postalinspectors.uspis.gov'
        for url in urls:
            yield Request(baseUrl + url['href'], callback=self.getInfo)

    def getInfo(self, response):
        try:
            soup = BeautifulSoup(response.body, 'lxml')
            item = BlUspsblacklistItem()
            item['title'] = soup.select('body > table > tr:nth-of-type(2) > td > p:nth-of-type(1) > b > font')[
                0].text.replace('  ', '').replace('\n', '').strip().replace('\r', ' ')
            item['violations'] = soup.select('table table table:nth-of-type(1) td:nth-of-type(3)')[0].text.replace('  ',
                                                                                                                   '').replace(
                '\n', '').strip().replace('\r', ' ')
            item['caseNo'] = soup.select('table table table:nth-of-type(2) td:nth-of-type(3)')[0].text.replace('  ',
                                                                                                               '').replace(
                '\n', '').strip().replace('\r', ' ')
            item['ncicNo'] = soup.select('table table table:nth-of-type(3) td:nth-of-type(3)')[0].text.replace('  ',
                                                                                                               '').replace(
                '\n', '').strip().replace('\r', ' ')
            item['fbiNo'] = soup.select('table table table:nth-of-type(4) td:nth-of-type(3)')[0].text.replace('  ',
                                                                                                              '').replace(
                '\n', '').strip().replace('\r', ' ')
            item['warrantNo'] = soup.select('table table table:nth-of-type(5) td:nth-of-type(3)')[0].text.replace('  ',
                                                                                                                  '').replace(
                '\n', '').strip().replace('\r', ' ')
            item['aliases'] = soup.select('table table table:nth-of-type(6) td:nth-of-type(3)')[0].text.replace('  ',
                                                                                                                '').replace(
                '\n', '').strip().replace('\r', ' ')
            item['dob'] = soup.select('table table table:nth-of-type(7) td:nth-of-type(3)')[0].text.replace('  ',
                                                                                                            '').replace(
                '\n', '').strip().replace('\r', ' ')
            item['description'] = soup.select('table table table:nth-of-type(8) td:nth-of-type(3)')[0].text.replace(
                '  ', '').replace('\n', '').strip().replace('\r', ' ')
            item['miscinfo'] = soup.select('table table table:nth-of-type(9) td:nth-of-type(3)')[0].text.replace('  ',
                                                                                                                 '').replace(
                '\n', '').strip().replace('\r', ' ')
            yield item
        except Exception as e:
            e
