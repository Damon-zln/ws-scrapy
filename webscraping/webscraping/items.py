# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CA_EngineerItem(Item):
    collection = 'ca_engineer'
    license_number = Field()
    name = Field()
    license_type = Field()
    license_status = Field()
    experience_completed = Field()
    previous_names = Field()
    address = Field()
    issue_date = Field()
    expiration_date = Field()


class CA_RealestateItem(Item):
    collection = 'ca_realestate'
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


class CA_ProlicItem(Item):
    collection = 'ca_prolic'
    license_number = Field()
    name = Field()
    license_type = Field()
    license_status = Field()
    experience_completed = Field()
    previous_names = Field()
    address = Field()
    issue_date = Field()
    expiration_date = Field()
