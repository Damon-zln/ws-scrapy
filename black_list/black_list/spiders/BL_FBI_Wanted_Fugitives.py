from bs4 import BeautifulSoup
from black_list.items import BLFBIWantedFugitives
from urllib.parse import urlencode
from scrapy import Spider, Request
import os


class BlfbiwantedfugitivesSpider(Spider):
    name = 'BL_FBI_Wanted_Fugitives'
    allowed_domains = ['www.fbi.gov']
    start_urls = [
        'https://www.fbi.gov/wanted/fugitives/@@castle.cms.querylisting/f7f80a1681ac41a08266bd0920c9d9d8?page=1']
    header = 'FullName|Aliases|Date(s)ofBirthUsed|Place of Birth|Hair|Eyes|Height|Wight|Sex|Race|Occupation|Nationality|Scars and Marks|NCIC|Remarks \n'

    def parse(self, response):
        with open(os.path.abspath('results/BL_FBI_Wanted_Fugitives.txt'), 'a', encoding='utf-8') as f:
            f.write(self.header)
        soup = BeautifulSoup(response.text, 'lxml')
        size = int(soup.select('p.right')[0].text.strip('Results: ').strip(' Items'))
        pages = size // 40 + 1
        base_url = 'https://www.fbi.gov/wanted/fugitives/@@castle.cms.querylisting/f7f80a1681ac41a08266bd0920c9d9d8?'
        for page in range(1, pages + 1):
            param = {'page': page}
            url = base_url + urlencode(param)
            yield Request(url, callback=self.get_page)

    def get_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        lis = soup.select('ul.castle-grid-block-xs-2.castle-grid-block-sm-2 li')
        for li in lis:
            url = li.a['href']
            yield Request(url, callback=self.get_info)

    def get_info(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        item = BLFBIWantedFugitives()
        item['name'] = soup.select('h1.documentFirstHeading')[0].text

        aliases = soup.find(text='Aliases:')
        if aliases is not None:
            item['aliases'] = soup.find(text='Aliases:').parent.next_sibling.next_sibling.text
        else:
            item['aliases'] = ''

        birth = soup.find(text='Date(s) of Birth Used')
        if birth is not None:
            item['birth'] = soup.find(text='Date(s) of Birth Used').parent.next_sibling.next_sibling.text
        else:
            item['birth'] = ''

        place_of_Birth = soup.find(text='Place of Birth')
        if place_of_Birth is not None:
            item['place_of_Birth'] = soup.find(text='Place of Birth').parent.next_sibling.next_sibling.text
        else:
            item['place_of_Birth'] = ''

        hair = soup.find(text='Hair')
        if hair is not None:
            item['hair'] = soup.find(text='Hair').parent.next_sibling.next_sibling.text
        else:
            item['hair'] = ''

        eyes = soup.find(text='Eyes')
        if eyes is not None:
            item['eyes'] = soup.find(text='Eyes').parent.next_sibling.next_sibling.text
        else:
            item['eyes'] = ''

        height = soup.find(text='Height')
        if height is not None:
            item['height'] = soup.find(text='Height').parent.next_sibling.next_sibling.text
        else:
            item['height'] = ''

        weight = soup.find(text='Weight')
        if weight is not None:
            item['weight'] = soup.find(text='Weight').parent.next_sibling.next_sibling.text
        else:
            item['weight'] = ''

        sex = soup.find(text='Sex')
        if sex is not None:
            item['sex'] = soup.find(text='Sex').parent.next_sibling.next_sibling.text
        else:
            item['sex'] = ''

        race = soup.find(text='Race')
        if race is not None:
            item['race'] = soup.find(text='Race').parent.next_sibling.next_sibling.text
        else:
            item['race'] = ''

        occupation = soup.find(text='Occupation')
        if occupation is not None:
            item['occupation'] = soup.find(text='Occupation').parent.next_sibling.next_sibling.text
        else:
            item['occupation'] = ''

        nationality = soup.find(text='Nationality')
        if nationality is not None:
            item['nationality'] = soup.find(text='Nationality').parent.next_sibling.next_sibling.text
        else:
            item['nationality'] = ''

        scars_and_marks = soup.find(text='Scars and Marks')
        if scars_and_marks is not None:
            item['scars_and_marks'] = soup.find(text='Scars and Marks').parent.next_sibling.next_sibling.text
        else:
            item['scars_and_marks'] = ''

        ncic = soup.find(text='NCIC')
        if ncic is not None:
            item['ncic'] = soup.find(text='NCIC').parent.next_sibling.next_sibling.text
        else:
            item['ncic'] = ''

        remarks = soup.find(text='Remarks:')
        if remarks is not None:
            item['remarks'] = soup.find(text='Remarks:').parent.next_sibling.next_sibling.text
        else:
            item['remarks'] = ''

        yield item
