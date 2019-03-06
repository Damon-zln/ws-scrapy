from bs4 import BeautifulSoup
from black_list.items import BLFBIWantedTerrorismItem
from scrapy import Spider, Request
import os


class BlFbiWantedTerrorismSpider(Spider):
    name = 'BL_FBI_Wanted_Terrorism'
    base_url = 'https://www.fbi.gov/wanted/terrorism/@@castle.cms.querylisting/55d8265003c84ff2a7688d7acd8ebd5a?page={page}'
    header = 'FullName|Aliases|Date(s)ofBirthUsed|Place of Birth|Hair|Eyes|Height|Build|Complexion|Sex|Race|Citizenship|Languages|Occupation|Nationality|Scars and Marks|NCIC|Reward|Remarks\n'

    def start_requests(self):
        with open(os.path.abspath('results/BL_FBI_Wanted_Terrorism.txt'), 'a', encoding='utf-8') as f:
            f.write(self.header)
        for i in range(1, 3):
            yield Request(url=self.base_url.format(page=i), callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        lis = soup.select('ul.castle-grid-block-xs-2.castle-grid-block-sm-2 li')
        for li in lis:
            url = li.a['href']
            yield Request(url, callback=self.get_info)

    def get_info(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        item = BLFBIWantedTerrorismItem()
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

        complexion = soup.find(text='Complexion')
        if complexion is not None:
            item['complexion'] = soup.find(text='Complexion').parent.next_sibling.next_sibling.text
        else:
            item['complexion'] = ''

        build = soup.find(text='Build')
        if build is not None:
            item['build'] = soup.find(text='Build').parent.next_sibling.next_sibling.text
        else:
            item['build'] = ''

        complexion = soup.find(text='Complexion')
        if complexion is not None:
            item['complexion'] = soup.find(text='Complexion').parent.next_sibling.next_sibling.text
        else:
            item['complexion'] = ''

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

        citizenship = soup.find(text='Citizenship')
        if citizenship is not None:
            item['citizenship'] = soup.find(text='Citizenship').parent.next_sibling.next_sibling.text
        else:
            item['citizenship'] = ''

        languages = soup.find(text='Languages')
        if languages is not None:
            item['languages'] = soup.find(text='Languages').parent.next_sibling.next_sibling.text
        else:
            item['languages'] = ''

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

        reward = soup.find(text='Reward')
        if reward is not None:
            item['reward'] = soup.find(text='Reward').parent.next_sibling.next_sibling.text
        else:
            item['reward'] = ''

        remarks = soup.find(text='Remarks:')
        if remarks is not None:
            item['remarks'] = soup.find(text='Remarks:').parent.parent.text.strip().strip('Remarks:').strip()
        else:
            item['remarks'] = ''

        yield item
