#!/usr/bin/env python3
# -*- coding:utf8 -*-
# @TIME  :2018/9/13 14:02
# @Author:dazhan
# @File  :CA_Prolic_professional_fiduciary.py

from scrapy import Request, Spider
from bs4 import BeautifulSoup
from webscraping.items import *


L = [chr(i) for i in range(97, 123)]
M = [chr(i) for i in range(97, 123)]


class ProlicSpider(Spider):
    name = 'CA_Prolic_professional_fiduciary'
    base_url = "http://www2.dca.ca.gov/pls/wllpub/WLLQRYNA$LCEV2.QueryList?P_QTE_CODE=PF&P_QTE_PGM_CODE=3108&P_NAME={lname}&P_RECORD_SET_SIZE=50&Z_ACTION=Find"
    next_url = "http://www2.dca.ca.gov/pls/wllpub/WLLQRYNA$LCEV2.QueryList?P_QTE_CODE=PF&P_QTE_PGM_CODE=3108&P_NAME={lname}&P_RECORD_SET_SIZE=50&Z_START={start}&Z_ACTION=Next"

    def start_requests(self):
        for l in L:
            for m in M:
                key = l + m
                yield Request(url=self.base_url.format(lname=key), callback=self.parse, meta={'key': key})

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        hs = soup.select('td[align="LEFT"] > a[href^="WLLQRYNA$LCEV2.QueryView"]')
        if hs:
            for i in hs:
                detail_url = "http://www2.dca.ca.gov/pls/wllpub/" + i['href']
                yield Request(url=detail_url, callback=self.parse_info)
            key = response.meta.get('key')
            yield Request(url=self.next_url.format(lname=key, start=1), callback=self.parse_next, meta={'key': key, 'start': 1})

    def parse_next(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        hs = soup.select('td[align="LEFT"] > a[href^="WLLQRYNA$LCEV2.QueryView"]')
        if hs:
            for i in hs:
                detail_url = "http://www2.dca.ca.gov/pls/wllpub/" + i['href']
                yield Request(url=detail_url, callback=self.parse_info)
            key = response.meta.get('key')
            start = response.meta.get('start') + 50
            yield Request(url=self.next_url.format(lname=key, start=start), callback=self.parse_next, meta={'key': key, 'start': start})

    def parse_info(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        trs = soup.select('tr[valign="TOP"]')
        prolic = CA_Prolic_professional_fiduciaryItem()
        for tr in trs:
            tr = tr.text
            if 'Licensee Name:' in tr:
                prolic['license_name'] = tr.replace('Licensee Name:', '').strip()
            if 'License Type:' in tr:
                prolic['license_type'] = tr.replace('License Type:', '').strip()
            if 'License Number:' in tr:
                prolic['license_number'] = tr.replace('License Number:', '').strip()
            if 'License Status:' in tr:
                prolic['license_status'] = tr.replace('License Status:', '').strip()
            if 'Expiration Date:' in tr:
                prolic['expiration_date'] = tr.replace('Expiration Date:', '').strip()
            if 'Issue Date:' in tr:
                prolic['issue_date'] = tr.replace('Issue Date:', '').strip()
            if 'Address:' in tr:
                prolic['address'] = tr.replace('Address:', '').strip()
            if 'City:' in tr:
                prolic['city'] = tr.replace('City:', '').strip()
            if 'State:' in tr:
                prolic['state'] = tr.replace('State:', '').strip()
            if 'Zip:' in tr:
                prolic['zip_code'] = tr.replace('Zip:', '').strip()
            if 'County:' in tr:
                prolic['county'] = tr.replace('County:', '').strip()
        yield prolic