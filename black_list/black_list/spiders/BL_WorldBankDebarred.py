from scrapy import Spider
from bs4 import BeautifulSoup
from black_list.items import BlworldbankdebarredItem
import os


class BlworldbankdebarredSpider(Spider):
    name = 'BL_WorldBankDebarred'
    allowed_domains = ['web.worldbank.org']
    start_urls = [
        'http://web.worldbank.org/external/default/main?theSitePK=84266&contentMDK=64069844&menuPK=116730&pagePK=64148989&piPK=64148984']
    header = 'FirmName|Address|Country|IneligibilityPeriodFrom|IneligibilityPeriodTo|Grounds \n'

    def parse(self, response):
        with open(os.path.abspath('results/BL_WorldBankDebarred.txt'), 'a', encoding='utf-8') as f:
            f.write(self.header)
        soup = BeautifulSoup(response.text, 'lxml')
        results1 = soup.select('.tableBorderGrey > tr')
        results1.pop(0)
        results1.pop(0)
        results1.pop(0)

        for tr in results1:
            item = BlworldbankdebarredItem()
            item['firmName'] = tr.select('td:nth-of-type(1)')[0].string.strip()
            item['address'] = tr.select('td:nth-of-type(2)')[0].text.replace('\n', ' ')
            item['country'] = tr.select('td:nth-of-type(3)')[0].string.strip()
            item['ineligibilityPeriodFrom'] = tr.select('td:nth-of-type(4)')[0].string.strip()
            item['ineligibilityPeriodTo'] = tr.select('td:nth-of-type(5)')[0].string.strip()
            item['grounds'] = tr.select('td:nth-of-type(6)')[0].string.strip()
            yield item
