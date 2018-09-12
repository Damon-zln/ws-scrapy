#!/usr/bin/env python3
# -*- coding:utf8 -*-
# @TIME  :2018/8/21 16:04
# @Author:dazhan
# @File  :CA_Realestate.py

from scrapy import Request, Spider
from bs4 import BeautifulSoup
from webscraping.items import *
import re


L = [chr(i) for i in range(97, 123)]
M = [chr(i) for i in range(97, 123)]


class RealestateSpider(Spider):
    name = 'CA_Realestate'
    base_url = "http://www2.dre.ca.gov/PublicASP/pplinfo.asp?NAV=1&LicenseeName={lname}"

    def start_requests(self):
        for l in L:
            for m in M:
                key = l + m
                yield Request(url=self.base_url.format(lname=key), callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        hs = soup.select('a[href^="pplinfo.asp?License_id="]')
        if hs:
            for i in hs:
                detail_url = 'http://www2.dre.ca.gov/PublicASP/' + i['href']
                yield Request(url=detail_url, callback=self.parse_info)
            page_re = re.compile('Matches>>')
            next_page = soup.find('a', text=page_re)
            if next_page:
                next_url = "http://www2.dre.ca.gov/PublicASP/" + next_page['href']
                yield Request(url=next_url, callback=self.parse)

    def parse_info(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        trs = soup.select('tr[valign="top"]')
        realestate = CA_RealestateItem()
        for i in trs:
            s = str(i.contents[1].font)
            s = s.split('size="2">')[1].split('</font>')[0].replace('<br/>', ' ').strip()
            if i.contents[0].text == 'License Type:':
                realestate['license_type'] = s
            if i.contents[0].text == 'Name:':
                realestate['name'] = s
            if i.contents[0].text == 'Mailing Address:':
                realestate['mailing_address'] = s
            if i.contents[0].text == 'License ID:':
                realestate['license_id'] = s
            if i.contents[0].text == 'Expiration Date:':
                realestate['expiration_date'] = s
            if i.contents[0].text == 'License Status:':
                realestate['license_status'] = s
            if i.contents[0].text == 'Salesperson License Issued:':
                realestate['sales_person_issue'] = s
            if i.contents[0].text == 'Broker License Issued:':
                realestate['broker_issue'] = s
            if i.contents[0].text == 'Former Name(s):':
                realestate['former_name'] = s
            if i.contents[0].text == 'Main Office:':
                realestate['main_office'] = s
        yield realestate


