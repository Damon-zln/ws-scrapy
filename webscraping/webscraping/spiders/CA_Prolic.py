#!/usr/bin/env python3
# -*- coding:utf8 -*-
# @TIME  :2018/10/17 9:42
# @Author:dazhan
# @File  :CA_Prolic.py

from scrapy import Request, Spider, FormRequest
from bs4 import BeautifulSoup
from webscraping.items import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
    'Referer': 'https://search.dca.ca.gov/?RD=Y'
}

sendKeys = [chr(i) for i in range(97, 123)]
boards = ['19', '28', '20', '21', '1', '3', '22,25', '35', '33', '9', '6', '24,26', '16', '4', '14', '7', '17', '30',
          '15', '18', '11', '31', '23', '12', '5', '13', '2', '29,32', '34', '10', '8']


class ProlicSpider(Spider):
    name = 'CA_Prolic'
    base_url = 'https://search.dca.ca.gov/results'

    def start_requests(self):
        for board in boards:
            for sendKey in sendKeys:
                for sendKey2 in sendKeys:
                    key = sendKey + sendKey2
                    yield FormRequest(url=self.base_url, headers=headers,
                                      formdata={'boardCode': board, 'lastName': key}, callback=self.parse_page)

    def parse_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        detail_urls = soup.select('ul[class="actions"] a')
        if detail_urls:
            for detail_url in detail_urls:
                url = "https://search.dca.ca.gov" + detail_url['href']
                yield Request(url=url, callback=self.parse_info)

    def parse_info(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        prolic = CA_ProlicItem()
        prolic['license_number'] = soup.select('h2[id="licDetail"]')[0].text.strip("Licensing details for:").strip()
        infos = soup.select('div[class="detailContainer"] p')
        if infos:
            for i in infos:
                i = i.get_text()
                if 'Name:' in i:
                    prolic['name'] = i.strip('Name:').strip()
                if 'License Type:' in i:
                    prolic['license_type'] = i.strip('License Type:').strip()
                if 'License Status:' in i:
                    prolic['license_status'] = i.strip('License Status:').strip()
                if 'Experience Completed:' in i:
                    prolic['experience_completed'] = i.strip('Experience Completed:').strip()
                if 'Previous Names:' in i:
                    prolic['previous_names'] = i.strip('Previous Names:').strip()
        address = soup.select('div[id="address"] p')
        if address:
            if len(address) >= 2:
                add_value = str(address[1])
                prolic['address'] = add_value.replace('<p class="wrapWithSpace">', '').strip('</p>').replace('<br/>', ', ')
        prolic['issue_date'] = soup.select('p[id="issueDate"]')[0].text
        prolic['expiration_date'] = soup.select('p[id="expDate"]')[0].text
        yield prolic


