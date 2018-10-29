#!/usr/bin/env python3
# -*- coding:utf8 -*-
# @TIME  :2018/8/20 15:22
# @Author:dazhan
# @File  :CA_Engineer.py

from scrapy import Request, Spider, FormRequest
from bs4 import BeautifulSoup
from webscraping.items import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
    'Referer': 'https://search.dca.ca.gov/?RD=Y'
}

sendKeys = [chr(i) for i in range(97, 123)]


class EngineerSpider(Spider):
    name = 'CA_Engineer'
    base_url = 'https://search.dca.ca.gov/results'

    def start_requests(self):
        for sendKey in sendKeys:
            for sendKey2 in sendKeys:
                key = sendKey + sendKey2
                yield FormRequest(url=self.base_url, headers=headers, formdata={'boardCode': '31', 'lastName': key}, callback=self.parse_page)

    def parse_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        detail_urls = soup.select('ul[class="actions"] a')
        if detail_urls:
            for detail_url in detail_urls:
                url = "https://search.dca.ca.gov" + detail_url['href']
                yield Request(url=url, callback=self.parse_info)

    def parse_info(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        engineer = CA_EngineerItem()
        engineer['license_number'] = soup.select('h2[id="licDetail"]')[0].text.strip("Licensing details for:").strip()
        infos = soup.select('div[class="detailContainer"] p')
        if infos:
            for i in infos:
                i = i.get_text()
                if 'Name:' in i:
                    engineer['name'] = i.strip('Name:').strip()
                if 'License Type:' in i:
                    engineer['license_type'] = i.strip('License Type:').strip()
                if 'License Status:' in i:
                    engineer['license_status'] = i.strip('License Status:').strip()
                if 'Experience Completed:' in i:
                    engineer['experience_completed'] = i.strip('Experience Completed:').strip()
                if 'Previous Names:' in i:
                    engineer['previous_names'] = i.strip('Previous Names:').strip()
        address = soup.select('div[id="address"] p')
        if address:
            if len(address) >= 2:
                add_value = str(address[1])
                engineer['address'] = add_value.replace('<p class="wrapWithSpace">', '').strip('</p>').replace('<br/>', ', ')
        engineer['issue_date'] = soup.select('p[id="issueDate"]')[0].text
        engineer['expiration_date'] = soup.select('p[id="expDate"]')[0].text
        yield engineer
