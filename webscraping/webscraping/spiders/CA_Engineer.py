#!/usr/bin/env python3
# -*- coding:utf8 -*-
# @TIME  :2018/8/20 15:22
# @Author:dazhan
# @File  :CA_Engineer.py

from scrapy import Request, Spider
from bs4 import BeautifulSoup
from webscraping.items import *
import re


L = [chr(i) for i in range(97, 123)]
M = [chr(i) for i in range(97, 123)]


class EngineerSpider(Spider):
    name = 'CA_Engineer'
    base_url = "http://www2.dca.ca.gov/pls/wllpub/WLLQRYNA$LCEV2.QueryList?P_QTE_CODE=ENG&P_QTE_PGM_CODE=7500&P_NAME={lname}&P_RECORD_SET_SIZE=50&Z_ACTION=Find"
    next_url = "http://www2.dca.ca.gov/pls/wllpub/WLLQRYNA$LCEV2.QueryList?P_QTE_CODE=ENG&P_QTE_PGM_CODE=7500&P_NAME={lname}&P_RECORD_SET_SIZE=50&Z_START={start}&Z_ACTION=Next"

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
        engineer = CA_EngineerItem()
        for tr in trs:
            tr = tr.text
            if 'Licensee Name:' in tr:
                engineer['license_name'] = re.sub(' {2,}', ' ', tr.replace('Licensee Name:', '').strip())
            if 'License Type:' in tr:
                engineer['license_type'] = tr.replace('License Type:', '').strip()
            if 'License Number:' in tr:
                engineer['license_number'] = tr.replace('License Number:', '').strip()
            if 'License Status:' in tr:
                engineer['license_status'] = tr.replace('License Status:', '').strip('Definition').strip()
            if 'Expiration Date:' in tr:
                engineer['expiration_date'] = re.sub(' {2,}', ' ', tr.replace('Expiration Date:', '').strip())
            if 'Address:' in tr:
                engineer['address'] = tr.replace('Address:', '').strip()
            if 'City:' in tr:
                engineer['city'] = tr.replace('City:', '').strip()
            if 'State:' in tr:
                engineer['state'] = tr.replace('State:', '').strip()
            if 'Zip:' in tr:
                engineer['zip_code'] = tr.replace('Zip:', '').strip()
            if 'County:' in tr:
                engineer['county'] = tr.replace('County:', '').strip()
            if 'Actions:' in tr:
                engineer['actions'] = tr.replace('Actions:', '').strip()
        yield engineer
