from scrapy import Spider
import os


class BlaustrailadfatSpider(Spider):
    name = 'BL_AustrailaDFAT'
    allowed_domains = ['www.dfat.gov.au']
    start_urls = [
        'https://dfat.gov.au/international-relations/security/sanctions/Documents/regulation8_consolidated.xls']

    def parse(self, response):
        with open(os.path.abspath('results/Austraila_DFAT_regulation8_consolidated.xls'), 'wb') as f:
            f.write(response.body)
