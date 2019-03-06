import time, os
from selenium import webdriver
from selenium.webdriver.support.select import Select

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://10.51.1.140:8080')
# chromeOptions.add_argument('headless')
chromeOptions.add_argument('--no-sandbox')
driver = webdriver.Chrome('D:\Projects\chromedriver.exe', chrome_options=chromeOptions)

# https://www.fincen.gov/financial_institutions/msb/msbstateselector.html


def scrape():
    for i in range(1, 11):
        driver.get('https://www.fincen.gov/fcn/financial_institutions/msb/msbstateselector.html')
        time.sleep(1)
        s = driver.find_element_by_id('SrchSrvOffered')
        Select(s).select_by_index(i)
        driver.find_element_by_name('submit').click()
        time.sleep(2)
        trs = driver.find_elements_by_css_selector('table[class="MSBregListtable"] tr')
        if trs:
            for tr in trs:
                print(tr.find_element_by_css_selector('td:nth-child(1)'))
    driver.quit()


if __name__ == '__main__':
    scrape()
