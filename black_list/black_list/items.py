# -*- coding: utf-8 -*-

from scrapy import Item, Field


class BLFBISeekingInfoItem(Item):
    collection = 'BL_FBI_Seeking_Info'
    name = Field()
    description = Field()
    birth = Field()
    place_of_Birth = Field()
    height = Field()
    weight = Field()
    build = Field()
    occupation = Field()
    hair = Field()
    eyes = Field()
    complexion = Field()
    sex = Field()
    nationality = Field()
    scars_and_marks = Field()
    remarks = Field()
    details = Field()
    reward = Field()
    citizenship = Field()
    languages = Field()


class BLFBIWantedTerrorismItem(Item):
    collection = 'BL_FBI_Wanted_Terrorism'
    name = Field()
    aliases = Field()
    birth = Field()
    place_of_Birth = Field()
    hair = Field()
    eyes = Field()
    height = Field()
    build = Field()
    complexion = Field()
    sex = Field()
    race = Field()
    citizenship = Field()
    languages = Field()
    occupation = Field()
    nationality = Field()
    scars_and_marks = Field()
    ncic = Field()
    reward = Field()
    remarks = Field()


class BLICEFugitivesListItem(Item):
    collection = 'BL_ICEFugitivesList'
    name = Field()
    offense = Field()
    aka = Field()
    sex = Field()
    dob = Field()
    pob = Field()
    complexion = Field()
    reward = Field()
    height = Field()
    weight = Field()
    eyes = Field()
    haia = Field()
    scars = Field()
    address = Field()
    synopsis = Field()
    warning = Field()


class BLMoneyLaunderingListItem(Item):
    collection = 'BL_MoneyLaunderingList'
    name = Field()
    finding = Field()
    notice_of_proposed = Field()
    final_rule = Field()
    rescinded = Field()


class BLUSForeignTerroristOrgItem(Item):
    collection = 'BL_US_Foreign_Terrorist_Org'
    date_designated = Field()
    designated_organization = Field()
    date_removed = Field()
    delisted_organization = Field()
    date_originally_designated = Field()


class BlChiefsOfStateItem(Item):
    collection = 'BL_Chiefs_of_State'
    country = Field()
    title = Field()
    name = Field()


class BlEuconsolidatedlistItem(Item):
    collection = 'BL_EUConsolidatedList'
    date = Field()
    id = Field()
    type = Field()
    legal_basis = Field()
    reg_date = Field()
    pdf_link = Field()
    programme = Field()
    remark = Field()
    id2 = Field()
    entity_id = Field()
    legal_basis2 = Field()
    reg_date2 = Field()
    pdf_link2 = Field()
    programme2 = Field()
    lastname = Field()
    firstname = Field()
    middlename = Field()
    wholename = Field()
    gender = Field()
    title = Field()
    function = Field()
    language = Field()
    id3 = Field()
    entity_id3 = Field()
    legal_basis3 = Field()
    reg_date3 = Field()
    pdf_link3 = Field()
    programme3 = Field()
    date3 = Field()
    place = Field()
    country = Field()
    id4 = Field()
    entity_id4 = Field()
    legal_basis4 = Field()
    reg_date4 = Field()
    pdf_link4 = Field()
    programme4 = Field()
    number = Field()
    country4 = Field()
    id5 = Field()
    entity_id5 = Field()
    legal_basis5 = Field()
    reg_date5 = Field()
    pdf_link5 = Field()
    programme5 = Field()
    country5 = Field()
    id6 = Field()
    entity_id6 = Field()
    legal_basis6 = Field()
    reg_date6 = Field()
    pdf_link6 = Field()
    programme6 = Field()
    number6 = Field()
    street = Field()
    zipcode = Field()
    city = Field()
    country6 = Field()
    other = Field()


class BLFBIWantedFugitives(Item):
    collection = 'BL_FBI_Wanted_Fugitives'
    name = Field()
    aliases = Field()
    birth = Field()
    place_of_Birth = Field()
    hair = Field()
    eyes = Field()
    height = Field()
    weight = Field()
    sex = Field()
    race = Field()
    occupation = Field()
    nationality = Field()
    scars_and_marks = Field()
    ncic = Field()
    remarks = Field()


class BlUspsblacklistItem(Item):
    collection = 'BL_USPSBlackList'
    title = Field()
    violations = Field()
    caseNo = Field()
    ncicNo = Field()
    fbiNo = Field()
    warrantNo = Field()
    aliases = Field()
    dob = Field()
    description = Field()
    miscinfo = Field()


class BlworldbankdebarredItem(Item):
    collection = 'BL_WorldBankDebarred'
    firmName = Field()
    address = Field()
    country = Field()
    ineligibilityPeriodFrom = Field()
    ineligibilityPeriodTo = Field()
    grounds = Field()
