import time, os
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://10.51.1.140:8080')
chromeOptions.add_argument('headless')
chromeOptions.add_argument('--no-sandbox')
prefs = {'download.default_directory': os.path.abspath('results')}
chromeOptions.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver.exe'), chrome_options=chromeOptions)

driver.command_executor._commands['send_command'] = ('POST', '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': os.path.abspath('results')}}
command_result = driver.execute('send_command', params)

driver.get('http://download.cms.gov/nppes/NPI_Files.html')
driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/div/table/tbody/tr[2]/td/div/ul/li/a').click()
time.sleep(30 * 60)
driver.quit()
