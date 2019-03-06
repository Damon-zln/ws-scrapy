# -*- coding: utf-8 -*-

from black_list.items import *
import os


class ScriptPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, BLFBISeekingInfoItem):
            with open(os.path.abspath('results/BL_FBI_Seeking_Info.txt'), 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|'
                        '%s|%s|%s|%s|%s|%s|%s|%s|%s \n' % (
                            item['name'], item['description'], item['birth'], item['place_of_Birth'], item['height'],
                            item['weight'], item['build'], item['occupation'], item['hair'], item['eyes'],
                            item['complexion'], item['sex'], item['nationality'], item['scars_and_marks'],
                            item['remarks'],
                            item['details'], item['reward'], item['citizenship'], item['languages']))

        if isinstance(item, BLFBIWantedTerrorismItem):
            with open(os.path.abspath('results/BL_FBI_Wanted_Terrorism.txt'), 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|'
                        '%s|%s|%s|%s|%s|%s|%s|%s|%s \n' % (
                            item['name'], item['aliases'], item['birth'], item['place_of_Birth'], item['hair'],
                            item['eyes'], item['height'], item['build'], item['complexion'], item['sex'],
                            item['race'], item['citizenship'], item['languages'], item['occupation'],
                            item['nationality'],
                            item['scars_and_marks'], item['ncic'], item['reward'], item['remarks']))

        if isinstance(item, BLICEFugitivesListItem):
            with open(os.path.abspath('results/BL_ICEFugitivesList.txt'), 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|'
                        '%s|%s|%s|%s|%s|%s \n' % (item['name'], item['offense'], item['aka'], item['sex'], item['dob'],
                                                  item['pob'], item['complexion'], item['reward'], item['height'],
                                                  item['weight'],
                                                  item['eyes'], item['haia'], item['scars'], item['address'],
                                                  item['synopsis'],
                                                  item['warning']))

        if isinstance(item, BLMoneyLaunderingListItem):
            with open(os.path.abspath('results/BL_MoneyLaunderingList.txt'), 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s\n' % (
                    item['name'], item['finding'], item['notice_of_proposed'], item['final_rule'], item['rescinded']))

        if isinstance(item, BLUSForeignTerroristOrgItem):
            with open(os.path.abspath('results/BL_US_Foreign_Terrorist_Org.txt'), 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s\n' % (
                    item['date_designated'], item['designated_organization'], item['date_removed'],
                    item['delisted_organization'], item['date_originally_designated']))

        if isinstance(item, BlChiefsOfStateItem):
            with open(os.path.abspath('results/BL_Chiefs_of_State.txt'), 'a') as f:
                f.write('%s|%s|%s \n' % (item['country'], item['title'], item['name']))

        if isinstance(item, BlEuconsolidatedlistItem):
            with open(os.path.abspath('results/BL_EUConsolidatedList.txt'), 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|'
                        '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|'
                        '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|'
                        '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|'
                        '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|'
                        '%s|%s|%s|%s|%s|%s|%s|%s\n' % (
                            item['date'], item['id'], item['type'], item['legal_basis'], item['reg_date'],
                            item['pdf_link'], item['programme'], item['remark'], item['id2'], item['entity_id'],
                            item['legal_basis2'], item['reg_date2'], item['pdf_link2'], item['programme2'],
                            item['lastname'],
                            item['firstname'], item['middlename'], item['wholename'], item['gender'], item['title'],
                            item['function'], item['language'], item['id3'], item['entity_id3'], item['legal_basis3'],
                            item['reg_date3'], item['pdf_link3'], item['programme3'], item['date3'], item['place'],
                            item['country'], item['id4'], item['entity_id4'], item['legal_basis4'], item['reg_date4'],
                            item['pdf_link4'], item['programme4'], item['number'], item['country4'], item['id5'],
                            item['entity_id5'], item['legal_basis5'], item['reg_date5'], item['pdf_link5'],
                            item['programme5'],
                            item['country5'], item['id6'], item['entity_id6'], item['legal_basis6'], item['reg_date6'],
                            item['pdf_link6'], item['programme6'], item['number6'], item['street'], item['zipcode'],
                            item['city'], item['country6'], item['other']))

        if isinstance(item, BLFBIWantedFugitives):
            with open(os.path.abspath('results/BL_FBI_Wanted_Fugitives.txt'), 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|'
                        '%s|%s|%s|%s|%s \n' % (
                            item['name'], item['aliases'], item['birth'], item['place_of_Birth'], item['hair'],
                            item['eyes'], item['height'], item['weight'], item['sex'], item['race'],
                            item['occupation'], item['nationality'], item['scars_and_marks'], item['ncic'],
                            item['remarks']))

        if isinstance(item, BlUspsblacklistItem):
            with open(os.path.abspath('results/BL_USPSBlackList.txt'), 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s|%s|%s|%s|%s|%s \n' % (item['title'], item['violations'], item['caseNo']
                                                              , item['ncicNo'], item['fbiNo'], item['warrantNo']
                                                              , item['aliases'], item['dob'], item['description']
                                                              , item['miscinfo']))

        if isinstance(item, BlworldbankdebarredItem):
            with open(os.path.abspath('results/BL_WorldBankDebarred.txt'), 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s|%s|%s|%s \n' % (item['firmName'], item['address'], item['country'],
                                                  item['ineligibilityPeriodFrom'],
                                                  item['ineligibilityPeriodTo'], item['grounds']))
