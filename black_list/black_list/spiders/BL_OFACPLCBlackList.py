from scrapy import Spider
import os


class BlOfacplcblacklistSpider(Spider):
    name = 'BL_OFACPLCBlackList'
    allowed_domains = ['www.treasury.gov']
    start_urls = ['https://www.treasury.gov/ofac/downloads/consolidated/cons_prim.csv',
                  'https://www.treasury.gov/ofac/downloads/consolidated/cons_add.csv',
                  'https://www.treasury.gov/ofac/downloads/consolidated/cons_alt.csv']

    def parse(self, response):
        if response.url == 'https://www.treasury.gov/ofac/downloads/consolidated/cons_prim.csv':
            with open(os.path.abspath('results/OFAC_PLC_cons_prim.txt'), 'ab') as f:
                f.write(response.body)
        if response.url == 'https://www.treasury.gov/ofac/downloads/consolidated/cons_add.csv':
            with open(os.path.abspath('results/OFAC_PLC_cons_add.txt'), 'ab') as f:
                f.write(response.body)
        if response.url == 'https://www.treasury.gov/ofac/downloads/consolidated/cons_alt.csv':
            with open(os.path.abspath('results/OFAC_PLC_cons_alt.txt'), 'ab') as f:
                f.write(response.body)
