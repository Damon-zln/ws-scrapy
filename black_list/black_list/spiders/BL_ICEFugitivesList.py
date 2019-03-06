from bs4 import BeautifulSoup
from black_list.items import BLICEFugitivesListItem
from scrapy import Spider, Request
import os


class BlIcefugitiveslistSpider(Spider):
    name = 'BL_ICEFugitivesList'
    allowed_domains = ['www.ice.gov']
    start_urls = ['https://www.ice.gov/most-wanted']
    header = 'Name|Status|Offense|AKA|Sex|DOB|POB|Complexion|Reward|Height|Weight|Eyes|Haia|Case Number|Scars|Address|Synopsis|Warning'

    def parse(self, response):
        with open(os.path.abspath('results/BL_ICEFugitivesList.txt'), 'a', encoding='utf-8') as f:
            f.write(self.header + '\n')
        soup = BeautifulSoup(response.body, 'lxml')
        tables = soup.select('.field-item')
        tables.pop(0)
        for table in tables:
            links = table.find_all(text='READ MORE')
            for link in links:
                yield Request(url='https://www.ice.gov%s' % (link.parent['href']), callback=self.get_info)

    def get_info(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        item = BLICEFugitivesListItem()
        item['name'] = ''
        item['offense'] = ''
        item['aka'] = ''
        item['sex'] = ''
        item['dob'] = ''
        item['pob'] = ''
        item['complexion'] = ''
        item['reward'] = ''
        item['height'] = ''
        item['weight'] = ''
        item['eyes'] = ''
        item['haia'] = ''
        item['scars'] = ''
        item['address'] = ''
        item['synopsis'] = ''
        item['warning'] = ''
        if soup.find(text='Name') is not None:
            item['name'] = soup.find(text='Name').parent.next_sibling.next_sibling.text
        if soup.select('div.wanted-for') is not None:
            item['offense'] = soup.select('div.wanted-for')[0].text
        if soup.find(text='Alias') is not None:
            item['aka'] = soup.find(text='Alias').parent.next_sibling.next_sibling.text
        if soup.find(text='Gender') is not None:
            item['sex'] = soup.find(text='Gender').parent.next_sibling.next_sibling.text
        if soup.find(text='Date of Birth') is not None:
            item['dob'] = soup.find(text='Date of Birth').parent.next_sibling.next_sibling.text
        if soup.find(text='Place of Birth') is not None:
            item['pob'] = soup.find(text='Place of Birth').parent.next_sibling.next_sibling.text
        if soup.find(text='Skin Tone') is not None:
            item['complexion'] = soup.find(text='Skin Tone').parent.next_sibling.next_sibling.text
        if soup.find(text='Reward') is not None:
            item['reward'] = soup.find(text='Reward').parent.next_sibling.next_sibling.text
        if soup.find(text='Height') is not None:
            item['height'] = soup.find(text='Height').parent.next_sibling.next_sibling.text
        if soup.find(text='Weight') is not None:
            item['weight'] = soup.find(text='Weight').parent.next_sibling.next_sibling.text
        if soup.find(text='Eyes') is not None:
            item['eyes'] = soup.find(text='Eyes').parent.next_sibling.next_sibling.text
        if soup.find(text='Hair') is not None:
            item['haia'] = soup.find(text='Hair').parent.next_sibling.next_sibling.text
        if soup.find(text='Scars/Marks') is not None:
            item['scars'] = soup.find(text='Scars/Marks').parent.next_sibling.next_sibling.text
        if soup.find(text='Last Known Location') is not None:
            item['address'] = soup.find(text='Last Known Location').parent.next_sibling.next_sibling.text
        values = soup.select('div[class="field-label"]')
        if values:
            for i in values:
                if "Summary:" in i.text:
                    item['synopsis'] = i.next_sibling.text
                if "Warning:" in i.text:
                    item['warning'] = i.next_sibling.text
        yield item
