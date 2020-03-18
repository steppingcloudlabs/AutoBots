import glob
import os
from datetime import datetime
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from dateutil.parser import parse
import subprocess
import pysftp
import time
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
today = datetime.now()
####################################################################################################################
#                                        | SFTP SERVER CONNECT |
####################################################################################################################


def connection_sftp():
    srv = pysftp.Connection(host="*********", username="*******",
                            password="********", cnopts=cnopts)

    # Get the directory and file
    data = srv.listdir('/outgoing/ec2comp/')
    srv.get('/outgoing/ec2comp/'+data[1], data[1])
    # for i in data:
    #     srv.get('/outgoing/ec2comp/'+i, './data/'+i)
    # Closes the connection
    srv.close()


try:
    connection_sftp()
    print("File downloaded")
except:
    pass

path = './'
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')


username = "********"
password = "*******"
company_name = "*******"
chromedriver = "./chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://hcm44preview.sapsf.com/login?company=cadilapharT1#/login")
# -----------------------------------------------------LOGIN-----------------------------------------------------
driver.find_element_by_xpath('//*[@id="__input1-inner"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="__input2-inner"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="__button2"]').click()

# ----------------------------------------------
driver.get(
    "https://hcm44preview.sapsf.com/xi/ui/ect/pages/admin/employeeImport/employeeImport.xhtml?")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="__link2"]').click()
table = driver.find_element_by_xpath(
    '//*[//*[@id="xfer_opt_div"]/table/tbody]')
table.find_elements_by_tag_name('tr')[4].find_element_by_xpath(
    '//*[@id="usreInboxXfer"]').click()
table.find_elements_by_tag_name('tr')[4].find_element_by_xpath(
    '//*[@id="usreEnrouteXfer"]').click()
table.find_elements_by_tag_name('tr')[4].find_element_by_xpath(
    '//*[@id="usreCompletedXfer"]').click()
table.find_elements_by_tag_name('tr')[4].find_element_by_xpath(
    '//*[@id="updateCompForm"]').click()
table.find_elements_by_tag_name('tr')[13].find_element_by_xpath(
    "//*[@id='compOption']/div[@id='comp_mass_update_option_div']/table/tbody/tr[1]/td/table/tbody/tr/td[2]/select[@id='templateId']/option[1]").click()
table = driver.find_element_by_xpath('//*[@id="7:_layoutTbl"]')
table = driver.find_element_by_xpath('//*[@id="7:_layoutTbl"]/tbody')
table.find_elements_by_tag_name('tr')[2].find_element_by_xpath(
    '//*[@id="8:"]').send_keys(os.getcwd()+"/"+result[0])
table.find_elements_by_tag_name('tr')[2].find_element_by_xpath(
    '//*[@id="import_btn"]').click()
