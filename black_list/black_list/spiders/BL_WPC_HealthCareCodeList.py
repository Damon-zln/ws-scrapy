from scrapy import Spider
import os


class BlWpcHealthcarecodelistSpider(Spider):
    name = 'BL_WPC_HealthCareCodeList'
    allowed_domains = ['www.nucc.org']
    start_urls = ['http://www.nucc.org/images/stories/CSV/nucc_taxonomy_181.csv']

    def parse(self, response):
        with open(os.path.abspath('results/nucc_taxonomy_181.csv.csv'), 'wb') as f:
            f.write(response.body)
