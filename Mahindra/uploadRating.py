import os
from datetime import datetime
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from dateutil.parser import parse
import time
import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
today = datetime.now()

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')


username = "******"
password = "******"
company_name = "****"
chromedriver = "./chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get(
    "https://performancemanager4.successfactors.com/")
# -----------------------------------------------------LOGIN-----------------------------------------------------

driver.find_element_by_xpath(
    '//*[@id = "__input0-inner"]').send_keys(company_name)
driver.find_element_by_xpath('//*[@id="__button0"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="__input1-inner"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="__input2-inner"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="__button2-content"]').click()
time.sleep(4)
# --------------------------------------------------TALENT POOL---------------------------------------------------
driver.get("https://performancemanager4.successfactors.com/sf/talentpool")
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
# ---------------------------------------------------ADD CANDIDATE-------------------------------------------------
driver.find_elements_by_xpath(
    "//*[contains(text(), 'National Sales Head (AD)')]")[0].click()
time.sleep(10)
driver.find_element_by_xpath('//*[@title="Add Talent Pool Nominee"]').click()
# ____________________CANDIDATE SEARCH_____________________________________
driver.find_element_by_xpath('//*[@placeholder="Search for incumbent"]').send_keys(
    '23199350')
driver.find_element_by_xpath(
    '//*[@placeholder="Search for incumbent"]').send_keys(Keys.DOWN)
driver.find_element_by_xpath(
    '//*[@placeholder="Search for incumbent"]').send_keys(Keys.RETURN)

driver.find_element_by_xpath(
    "//*[contains(text(), 'Next')]").click()
