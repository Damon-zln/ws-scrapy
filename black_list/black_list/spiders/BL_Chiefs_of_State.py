from scrapy import Spider, Request
from black_list.items import BlChiefsOfStateItem
from bs4 import BeautifulSoup
import os


class BlchiefsOfStateSpider(Spider):
    name = 'BL_Chiefs_of_State'
    allowed_domains = ['www.cia.gov']
    start_urls = ['https://www.cia.gov/library/publications/world-leaders-1']
    header = 'country|title|name \n'

    def parse(self, response):
        with open(os.path.abspath('results/BL_Chiefs_of_State.txt'), 'a', encoding='utf-8') as f:
            f.write(self.header)
        hrefs = response.css('#cosCountryList li a::attr(href)').extract()
        for href in hrefs:
            url = self.start_urls[0] + '/' + href
            yield Request(url, callback=self.getInfo)

    def getInfo(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        lis = soup.select('#countryOutput > div > div > ul > li')
        for li in lis:
            item = BlChiefsOfStateItem()
            item['country'] = soup.select('td.countryName')[0].text
            item['title'] = li.select('#chiefsOutput > div > div:nth-of-type(1) > span > span')[0].text
            item['name'] = li.select('#chiefsOutput > div > div:nth-of-type(2)')[0].text.strip()
            yield item
