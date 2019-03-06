from bs4 import BeautifulSoup
from black_list.items import BlEuconsolidatedlistItem
from scrapy import Spider
import os


class BleuconsolidatedlistSpider(Spider):
    name = 'BL_EUConsolidatedList'
    allowed_domains = ['ec.europa.eu']
    start_urls = ['http://ec.europa.eu/external_relations/cfsp/sanctions/list/version4/global/global.xml']
    header = 'Date|Id|Type|legal_basis|reg_date|pdf_link|programme|remark|Id2|Entity_id|legal_basis2|reg_date2|pdf_link2|programme2|LASTNAME|FIRSTNAME|MIDDLENAME|WHOLENAME|GENDER|TITLE|FUNCTION|LANGUAGE|Id3|Entity_id3|legal_basis3|reg_date3|pdf_link3|programme3|DATE3|PLACE|COUNTRY|Id4|Entity_id4|legal_basis4|reg_date4|pdf_link4|programme4|NUMBER|COUNTRY4|Id5|Entity_id5|legal_basis5|reg_date5|pdf_link5|programme5|COUNTRY5|Id6|Entity_id6|legal_basis6|reg_date6|pdf_link6|programme6|NUMBER6|STREET|ZIPCODE|CITY|COUNTRY6|OTHER \n'

    def parse(self, response):
        with open(os.path.abspath('results/BL_EUConsolidatedList.txt'), 'a', encoding='utf-8') as f:
            f.write(self.header)
        soup = BeautifulSoup(response.text, 'xml')
        entities = soup.find_all(name='ENTITY')
        for entity in entities:
            item = BlEuconsolidatedlistItem()
            item['date'] = soup.WHOLE['Date']
            item['id'] = entity['Id']
            item['type'] = entity['Type']
            item['legal_basis'] = entity['legal_basis']
            item['reg_date'] = entity['reg_date']
            item['pdf_link'] = entity['pdf_link']
            item['programme'] = entity['programme']
            item['remark'] = entity['remark']
            name1 = entity.NAME
            item['id2'] = name1['Id']
            item['entity_id'] = name1['Entity_id']
            item['legal_basis2'] = name1['legal_basis']
            item['reg_date2'] = name1['reg_date']
            item['pdf_link2'] = name1['pdf_link']
            item['programme2'] = name1['programme']
            item['lastname'] = name1.LASTNAME.text
            item['firstname'] = name1.FIRSTNAME.text
            item['middlename'] = name1.MIDDLENAME.text
            item['wholename'] = name1.WHOLENAME.text
            item['gender'] = name1.GENDER.text
            item['title'] = name1.TITLE.text
            item['function'] = name1.FUNCTION.text
            item['language'] = name1.LANGUAGE.text
            birth = entity.BIRTH
            if birth is not None:
                item['id3'] = birth['Id']
                item['entity_id3'] = birth['Entity_id']
                item['legal_basis3'] = birth['legal_basis']
                item['reg_date3'] = birth['reg_date']
                item['pdf_link3'] = birth['pdf_link']
                item['programme3'] = birth['programme']
                item['date3'] = birth.DATE.text
                item['place'] = birth.PLACE.text
                item['country'] = birth.COUNTRY.text
            else:
                item['id3'] = ''
                item['entity_id3'] = ''
                item['legal_basis3'] = ''
                item['reg_date3'] = ''
                item['pdf_link3'] = ''
                item['programme3'] = ''
                item['date3'] = ''
                item['place'] = ''
                item['country'] = ''
            passport = entity.PASSPORT
            if passport is not None:
                item['id4'] = passport['Id']
                item['entity_id4'] = passport['Entity_id']
                item['legal_basis4'] = passport['legal_basis']
                item['reg_date4'] = passport['reg_date']
                item['pdf_link4'] = passport['pdf_link']
                item['programme4'] = passport['programme']
                item['number'] = passport.NUMBER.text
                item['country4'] = passport.COUNTRY.text
            else:
                item['id4'] = ''
                item['entity_id4'] = ''
                item['legal_basis4'] = ''
                item['reg_date4'] = ''
                item['pdf_link4'] = ''
                item['programme4'] = ''
                item['number'] = ''
                item['country4'] = ''
            citizen = entity.CITIZEN
            if citizen is not None:
                item['id5'] = citizen['Id']
                item['entity_id5'] = citizen['Entity_id']
                item['legal_basis5'] = citizen['legal_basis']
                item['reg_date5'] = citizen['reg_date']
                item['pdf_link5'] = citizen['pdf_link']
                item['programme5'] = citizen['programme']
                item['country5'] = citizen.COUNTRY.text
            else:
                item['id5'] = ''
                item['entity_id5'] = ''
                item['legal_basis5'] = ''
                item['reg_date5'] = ''
                item['pdf_link5'] = ''
                item['programme5'] = ''
                item['country5'] = ''
            address = entity.ADDRESS
            if address is not None:
                item['id6'] = address['Id']
                item['entity_id6'] = address['Entity_id']
                item['legal_basis6'] = address['legal_basis']
                item['reg_date6'] = address['reg_date']
                item['pdf_link6'] = address['pdf_link']
                item['programme6'] = address['programme']
                item['number6'] = address.NUMBER.text
                item['street'] = address.STREET.text
                item['zipcode'] = address.ZIPCODE.text
                item['city'] = address.CITY.text
                item['country6'] = address.COUNTRY.text
                item['other'] = address.OTHER.text
            else:
                item['id6'] = ''
                item['entity_id6'] = ''
                item['legal_basis6'] = ''
                item['reg_date6'] = ''
                item['pdf_link6'] = ''
                item['programme6'] = ''
                item['number6'] = ''
                item['street'] = ''
                item['zipcode'] = ''
                item['city'] = ''
                item['country6'] = ''
                item['other'] = ''
            yield item
