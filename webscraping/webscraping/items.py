# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CA_EngineerItem(Item):
    collection = 'ca_engineer'
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
    collection = 'ca_prolic_registered_pharmacist'
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
    collection = 'ca_prolic_pharmacy_technician'
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


class CA_Prolic_acupunctureItem(Item):
    collection = 'ca_prolic_acupuncture'
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


class CA_Prolic_architectItem(Item):
    collection = 'ca_prolic_architect'
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


class CA_Prolic_courtReporterItem(Item):
    collection = 'ca_prolic_courtReporter'
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


class CA_Prolic_professional_fiduciaryItem(Item):
    collection = 'ca_prolic_professional_fiduciary'
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


class CA_Prolic_hearing_aid_dispenserItem(Item):
    collection = 'ca_prolic_hearing_aid_dispenser'
    license_name = Field()
    license_type = Field()
    license_number = Field()
    license_status = Field()
    expiration_date = Field()
    issue_date = Field()
    address1 = Field()
    address2 = Field()
    city = Field()
    state = Field()
    zip_code = Field()
    county = Field()
    actions = Field()


class CA_Prolic_accountancyItem(Item):
    collection = 'ca_prolic_accountancy'
    license_name = Field()
    license_type = Field()
    license_number = Field()
    license_status = Field()
    experience_completed = Field()
    expiration_date = Field()
    issue_date = Field()
    address = Field()
    city = Field()
    state = Field()
    zip_code = Field()
    county = Field()
    actions = Field()


class CA_Prolic_automotiveItem(Item):
    collection = 'ca_prolic_automotive'
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



