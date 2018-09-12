# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CA_EngineerItem(Item):
    collection = 'engineer'
    license_name = Field()
    license_type = Field()
    license_number = Field()
    license_status = Field()
    expiration_date = Field()
    address = Field()
    city = Field()
    state = Field()
    zip_code = Field()
    county = Field()
    actions = Field()


class CA_Prolic_registered_pharmacistItem(Item):
    collection = 'registered_pharmacist'
    license_name = Field()
    license_type = Field()
    license_number = Field()
    license_status = Field()
    expiration_date = Field()
    issue_date = Field()
    address = Field()
    city = Field()
    state = Field()
    zip_code = Field()
    county = Field()
    actions = Field()


class CA_Prolic_pharmacy_technician(Item):
    collection = 'pharmacy_technician'
    license_name = Field()
    license_type = Field()
    license_number = Field()
    license_status = Field()
    expiration_date = Field()
    issue_date = Field()
    address = Field()
    city = Field()
    state = Field()
    zip_code = Field()
    county = Field()
    actions = Field()


class CA_Prolic_automotiveItem(Item):
    collection = 'automotive'
    license_name = Field()
    license_type = Field()
    license_number = Field()
    license_status = Field()
    expiration_date = Field()
    address = Field()
    city = Field()
    state = Field()
    zip_code = Field()
    county = Field()


class CA_RealestateItem(Item):
    collection = 'realestate2'
    license_type = Field()
    name = Field()
    mailing_address = Field()
    license_id = Field()
    expiration_date = Field()
    license_status = Field()
    broker_issue = Field()
    sales_person_issue = Field()
    former_name = Field()
    main_office = Field()



