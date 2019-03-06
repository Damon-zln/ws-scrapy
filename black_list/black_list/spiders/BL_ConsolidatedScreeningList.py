from scrapy import Spider
import os


class BlconsolidatedscreeninglistSpider(Spider):
    name = 'BL_ConsolidatedScreeningList'
    allowed_domains = ['export.gov']
    start_urls = ['https://api.trade.gov/consolidated_screening_list/search.csv?api_key=OHZYuksFHSFao8jDXTkfiypO']

    def parse(self, response):
        with open(os.path.abspath('results/screening_list_consolidated.csv'), 'ab') as f:
            f.write(response.body)
