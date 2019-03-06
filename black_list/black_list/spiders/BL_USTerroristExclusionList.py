from scrapy import Spider
from bs4 import BeautifulSoup
import os


class BlUsterroristexclusionlistSpider(Spider):
    name = 'BL_USTerroristExclusionList'
    allowed_domains = ['www.state.gov']
    start_urls = ['http://www.state.gov/j/ct/rls/other/des/123086.htm']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.select('#centerblock > ul:nth-of-type(3) li')
        with open(os.path.abspath('results/BL_USTerroristExclusionList.txt'), 'a', encoding='utf-8') as f:
            for i in content:
                f.write(i.text.strip() + '\n')
