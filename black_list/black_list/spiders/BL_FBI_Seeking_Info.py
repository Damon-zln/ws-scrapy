from bs4 import BeautifulSoup
from black_list.items import BLFBISeekingInfoItem
from scrapy import Spider, Request
import os


class BlFbiSeekingInfoSpider(Spider):
    name = 'BL_FBI_Seeking_Info'
    base_url = "https://www.fbi.gov/wanted/seeking-information/@@castle.cms.querylisting/5abe9de716674277b799bc03b34e1aa4?page={page}"
    header = 'Name|description|Date(s)ofBirthUsed|PlaceofBirth|Height|Weight|Build|Occupations|Hair|Eyes|Complexion|Sex|Nationality|ScarsAndMarks|remarks|details|reward|Citizenship|Languages \n'

    def start_requests(self):
        with open(os.path.abspath('results/BL_FBI_Seeking_Info.txt'), 'a') as f:
            f.write(self.header)
        for i in range(1, 5):
            yield Request(url=self.base_url.format(page=i), callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        lis = soup.select('ul.castle-grid-block-xs-2.castle-grid-block-sm-2 li')
        for li in lis:
            url = li.a['href']
            yield Request(url, self.get_info)

    def get_info(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        item = BLFBISeekingInfoItem()
        item['name'] = soup.select('h1.documentFirstHeading')[0].text

        description = list(soup.select('div.col-lg-12.wanted-person-wrapper')[0].p.children)[::2]
        item['description'] = ''
        for i in description:
            item['description'] = item['description'] + i + ' '

        birth = soup.find(text='Date(s) of Birth Used')
        if birth is not None:
            item['birth'] = birth.parent.next_sibling.next_sibling.text
        else:
            item['birth'] = ''

        place_of_Birth = soup.find(text='PlaceofBirth')
        if place_of_Birth is not None:
            item['place_of_Birth'] = place_of_Birth.parent.next_sibling.next_sibling.text
        else:
            item['place_of_Birth'] = ''

        height = soup.find(text='Height')
        if height is not None:
            item['height'] = height.parent.next_sibling.next_sibling.text
        else:
            item['height'] = ''

        weight = soup.find(text='Weight')
        if weight is not None:
            item['weight'] = weight.parent.next_sibling.next_sibling.text
        else:
            item['weight'] = ''

        build = soup.find(text='Build')
        if build is not None:
            item['build'] = build.parent.next_sibling.next_sibling.text
        else:
            item['build'] = ''

        occupation = soup.find(text='Occupations')
        if occupation is not None:
            item['occupation'] = occupation.parent.next_sibling.next_sibling.text
        else:
            item['occupation'] = ''

        hair = soup.find(text='Hair')
        if hair is not None:
            item['hair'] = hair.parent.next_sibling.next_sibling.text
        else:
            item['hair'] = ''

        eyes = soup.find(text='Eyes')
        if eyes is not None:
            item['eyes'] = eyes.parent.next_sibling.next_sibling.text
        else:
            item['eyes'] = ''

        complexion = soup.find(text='Complexion')
        if complexion is not None:
            item['complexion'] = complexion.parent.next_sibling.next_sibling.text
        else:
            item['complexion'] = ''

        sex = soup.find(text='Sex')
        if sex is not None:
            item['sex'] = sex.parent.next_sibling.next_sibling.text
        else:
            item['sex'] = ''

        nationality = soup.find(text='Nationality')
        if nationality is not None:
            item['nationality'] = nationality.parent.next_sibling.next_sibling.text
        else:
            item['nationality'] = ''

        scars_and_marks = soup.find(text='Scars and Marks')
        if scars_and_marks is not None:
            item['scars_and_marks'] = scars_and_marks.parent.next_sibling.next_sibling.text
        else:
            item['scars_and_marks'] = ''

        remarks = soup.find(text='Remarks:')
        if remarks is not None and remarks.parent.next_sibling.next_sibling is not None:
            item['remarks'] = remarks.parent.next_sibling.next_sibling.text
        else:
            item['remarks'] = ''

        details = soup.find(text='Details:')
        if details is not None:
            ps = details.parent.parent.find_all(name='p')
            item['details'] = ''
            for p in ps:
                item['details'] = item['details'] + p.text.replace('\n', '') + ' '
        else:
            item['details'] = ''

        reward = soup.find(text='Reward:')
        if reward is not None:
            item['reward'] = reward.parent.next_sibling.next_sibling.text
        else:
            item['reward'] = ''

        citizenship = soup.find(text='Citizenship')
        if citizenship is not None:
            item['citizenship'] = citizenship.parent.next_sibling.next_sibling.text
        else:
            item['citizenship'] = ''

        languages = soup.find(text='Languages')
        if languages is not None:
            item['languages'] = languages.parent.next_sibling.next_sibling.text
        else:
            item['languages'] = ''

        yield item
