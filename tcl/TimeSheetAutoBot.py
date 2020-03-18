import csv
from selenium.webdriver.common.by import By
import os
from datetime import date, datetime, time, timedelta
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from dateutil.parser import parse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import pysftp
import glob
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

proxyIndex = 1

username = "adminth"
password = "Tcl@1234"
company_name = "TATAComm"


def worker(driver, user_time_data, id_user, url_user):
    # proxy code----------------
    proxy(driver, user_time_data, id_user)
    currentUrl = driver.current_url
    if ("companyEntry" in currentUrl):
        login(driver, company_name, username, password)
        time.sleep(10)
        worker(driver, user_time_data, id_user, url_user)
    else:
        driver.get(url_user)
        time.sleep(5)
        weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        j = 4
        for idx, row in user_time_data.iterrows():
            print("Doing row: ", idx)
            userid = row['userId']
            projectid = row['Project (Project Name)']
            taskid = row['Task (Task Name)']
            countryid = row['Facility Country (Label)']
            workname = row['timeType (Label)']
            hrs = row['quantityInHours']
            hrs = hrs*60
            hour = int(hrs//60)
            print(hour)
            mins = int(hrs % 60)
            print(mins)
            day = row['startDate']
            i = weekdays.index(day)+1
            if(i == 7):
                random = i-1
            else:
                random = i+3
            time.sleep(6)
            driver.find_element_by_xpath(
                '/html/body/div['+str(j)+']/div/div[2]/div[2]/div[4]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div['+str(random)+']/div').click()
            # ----------------------------------------------------details-------------------------------
            time.sleep(3)
            container = driver.find_element_by_id('container')
            # wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[2]/div[3]/div[4]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div['+str(i)+']/div'))).click()
            time.sleep(3)
            driver.find_element_by_xpath(
                '/html/body/div['+str(j)+']/div/div[2]/div[2]/div[4]/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div['+str(i)+']/div').click()
            time.sleep(2)
            driver.find_element_by_xpath(
                '/html/body/div['+str(j)+']/div/div[2]/div[2]/div[4]/div/div/div/div[2]/div[1]/div/div/div[4]/div[1]/div['+str(i)+']/button[2]/span/span[2]').click()
            time.sleep(2)
            # driver.find_element_by_xpath('html/body/div[4]/div/div[2]/div[3]/div[4]/div/div/div/div[2]/div[1]/div/div/div[4]/div[1]/div['+str(i)+']/button[2]/span/span[2]').click()
            time.sleep(3)
            # /html/body/div[4]/div/div[2]/div[2]/div[4]/div/div/div/div[2]/div[1]/div/div/div[4]/div[1]/div[7]/div/div[1]/div[2]/div/div/div/div/table
            table = driver.find_element_by_xpath(
                '/html/body/div['+str(j)+']/div/div[2]/div[2]/div[4]/div/div/div/div[2]/div[1]/div/div/div[4]/div[1]/div['+str(i)+']/div/div[1]/div[2]/div/div/div/div/table/tbody')
            rows = table.find_elements_by_tag_name('tr')
            r_no = len(rows)
            # wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div[2]/div[3]/div[4]/div/div/div/div[2]/div[1]/div/div/div[4]/div[1]/div['+str(i)+']/div/div[1]/div[2]/div/div/div/div/table/tbody/tr[2]/th[1]/a[1]'))).click()
            # /html/body/div[4]/div/div[2]/div[2]/div[4]/div/div/div/div[2]/div[1]/div/div/div[4]/div[1]/div[7]/div/div[1]/div[2]/div/div/div/div/table/tbody/tr[2]/th[1]/a[1]

            driver.find_element_by_xpath('/html/body/div['+str(j)+']/div/div[2]/div[2]/div[4]/div/div/div/div[2]/div[1]/div/div/div[4]/div[1]/div['+str(
                i)+']/div/div[1]/div[2]/div/div/div/div/table/tbody/tr['+str(r_no)+']/th[1]/a[1]').click()

            # ------------------------------------------updation table----------------------------
            table = driver.find_element_by_css_selector(
                '.layoutTable.center_align')
            tbody = table.find_element_by_tag_name('tbody')
            data_row = tbody.find_elements_by_tag_name('tr')
            person = data_row[2].find_elements_by_tag_name('td')[1]
            person.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(Keys.BACKSPACE)
            time.sleep(8)

            person.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(userid)
            time.sleep(2)
            person.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            person.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(Keys.ENTER)

            # --------------------------------------projectID-------------------------
            table = driver.find_element_by_css_selector(
                '.layoutTable.center_align')
            tbody = table.find_element_by_tag_name('tbody')
            data_row = tbody.find_elements_by_tag_name('tr')

            project = data_row[3].find_elements_by_tag_name('td')[1]
            project.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(Keys.BACKSPACE)

            time.sleep(6)
            project.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(projectid)
            time.sleep(6)
            project.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            project.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(Keys.ENTER)

            # time.sleep(6)
            # -----------------------------------------------taskid----------------------------
            table = driver.find_element_by_css_selector(
                '.layoutTable.center_align')
            tbody = table.find_element_by_tag_name('tbody')
            data_row = tbody.find_elements_by_tag_name('tr')

            task = data_row[4].find_elements_by_tag_name('td')[1]
            task.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(Keys.BACKSPACE)

            time.sleep(6)
            task.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(taskid)
            time.sleep(6)
            task.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            task.find_element_by_xpath(
                './/div/span[1]/div/div[1]/div/span[1]/span[1]/span/input').send_keys(Keys.ENTER)

            # ------------------------------------------------------country--------------------------------------
            table = driver.find_element_by_css_selector(
                '.layoutTable.center_align')
            tbody = table.find_element_by_tag_name('tbody')
            data_row = tbody.find_elements_by_tag_name('tr')

            country = data_row[9].find_elements_by_tag_name('td')[1]
            country.find_element_by_xpath(
                './/div/span[1]/span[1]/span/input').send_keys(Keys.BACKSPACE)

            time.sleep(3)
            country.find_element_by_xpath(
                './/div/span[1]/span[1]/span/input').send_keys(countryid)
            time.sleep(3)
            country.find_element_by_xpath(
                './/div/span[1]/span[1]/span/input').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            country.find_element_by_xpath(
                './/div/span[1]/span[1]/span/input').send_keys(Keys.ENTER)

            # -------------------------------------------Notes-------------------------
            table = driver.find_element_by_css_selector(
                '.layoutTable.center_align')
            tbody = table.find_element_by_tag_name('tbody')
            data_row = tbody.find_elements_by_tag_name('tr')

            notes = data_row[14].find_elements_by_tag_name('td')[1]
            notes.find_element_by_xpath(
                './/div/span[1]/span/span/div/textarea').send_keys("testing")
            time.sleep(3)
            # -----------------------------------------------Type-------------------
            table = driver.find_element_by_css_selector(
                '.layoutTable.center_align')
            tbody = table.find_element_by_tag_name('tbody')
            data_row = tbody.find_elements_by_tag_name('tr')
            list1 = ['Overtime (1.5)', 'Overtime double (2)',
                     'Time in Lieu(1.5)', 'Time in Lieu(2)', 'Working Time']

            worktype = data_row[0].find_elements_by_tag_name('td')[1]

            index = list1.index(workname)+1
            worktype.find_element_by_xpath(
                './/div/span[1]/span[1]/span/span').click()

            worktype.find_element_by_xpath(
                '/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/ul/li['+str(index)+']').click()

            # -----------------------------------------------------hours-----------------------------------------
            table = driver.find_element_by_css_selector(
                '.layoutTable.center_align')
            tbody = table.find_element_by_tag_name('tbody')
            data_row = tbody.find_elements_by_tag_name('tr')

            hours = data_row[1].find_elements_by_tag_name('td')[1]
            time.sleep(3)
            hours.find_element_by_xpath(
                './/div/span[1]/div/div[1]/input[1]').send_keys(hour)
            time.sleep(3)
            hours.find_element_by_xpath(
                './/div/span[1]/div/div[1]/input[2]').send_keys(mins)
            time.sleep(3)
            hours.find_element_by_xpath(
                './/div/span[1]/div/div[1]/input[2]').send_keys(Keys.ENTER)

            # time.sleep(6)
            driver.find_element_by_xpath(
                '/html/body/div[9]/div/div/div/div[2]/div/div[2]/div[2]/div/span/span/button').click()
            time.sleep(5)
            # container.find_element_by_xpath('.//div[3]/div[4]/div/div/div/div[2]/div[1]/div/div/div[4]/div[1]/div['+str(i)+']/button[2]/span/span[2]').click()
            j = 5
            driver.find_element_by_xpath('/html/body/div['+str(j)+']/div/div[2]/div[2]/div[4]/div/div/div/div[2]/div[1]/div/div/div[4]/div[1]/div['+str(i)+']/button[2]/span/span[2]').click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[4]/div/div/div/div[2]/div[1]/div/div/div[5]/div[2]/span[7]/span/button').click()
        time.sleep(15)
        driver.find_element_by_xpath(
            '/html/body/div[9]/div/div/div/div[2]/div/div/div/div/div[3]/div/span[2]/span/span/button').click()
        #worker(driver, user_time_data, id_user, url_user)


def proxy(driver, user_time_data, id_user):
    time.sleep(5)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div/div/div/section/div/div[2]/section/div[2]/div/div/div[1]/div/div/div/div[3]/div[4]/button/div').click()
    time.sleep(5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[5]/div/div/div/ul/a['+str(proxyIndex)+']').click()
    time.sleep(5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[7]/section/div/div/div/div/div/input').send_keys(str(id_user))
    time.sleep(5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[7]/section/div/div/div/div/div/input').send_keys(Keys.ARROW_DOWN)
    time.sleep(5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[7]/section/div/div/div/div/div/input').send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[7]/footer/div/button[2]').click()
    time.sleep(5)


def master(driver, grouped_user, unique_user):
    for i in unique_user:
        print(i)
        # url_user = "https://performancemanager4.successfactors.com/xi/ui/ect/pages/attendance/timeSheet.xhtml?selected_user=" + \
        #     str(i)
        url_user = "https://performancemanager41.successfactors.com/xi/ui/ect/pages/attendance/timeSheet.xhtml"
        user_time_data = grouped_user.get_group(i)
        worker(driver, user_time_data, i, url_user)


def login(driver, company_name, username, password):
    driver.find_element_by_xpath(
        '//*[@id="__input0-inner"]').send_keys(company_name)
    driver.find_element_by_xpath('//*[@id="__button0-img"]').click()

    time.sleep(5)
    # -----------------------------------------------------LOGIN-----------------------------------------------------
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath(
        '/html/body/form/div[1]/div/div[4]/div[2]/table/tbody/tr/td[1]/input').click()

####################################################################################################################
# | SFTP SERVER CONNECT |
####################################################################################################################


def connection_sftp():
    srv = pysftp.Connection(host="**********", username="**********",
                            password="***********", cnopts=cnopts)

    # Get the directory and file
    data = srv.listdir('/timesheetbot')

    srv.get('/timesheetbot/'+data[0], "data.csv")
    # for i in data:
    # srv.get('/outgoing/ec2comp/'+i, './data/'+i)
    # Closes the connection
    srv.close()


if __name__ == "__main__":

    # os.remove("data.csv")
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    username = "*****"
    password = "*******"
    company_name = "*******"
    chromedriver = "./chromedriver"
    try:
        connection_sftp()
        print("File downloaded")
    except:
        pass

    path = './'
    extension = 'csv'
    os.chdir(path)
    filename = glob.glob('*.{}'.format(extension))
    driver = webdriver.Chrome(chromedriver)
    driver.get(
        "https://performancemanager4.successfactors.com/sf/start/#/companyCheck")
    login(driver, company_name, username, password)
    time.sleep(5)

    # ------------------------------------------------------------------------------------------------

    data = pd.read_csv("data.csv")
    unwantedTimeType = [
        'Overtime (1.5)', 'Overtime double (2)', 'Time in Lieu(1.5)', 'Time in Lieu(2)']
    data = data[~data['timeType (Label)'].isin(unwantedTimeType)]
    print(data)
    unique_user = data["userId"].unique()
    data["startDate"] = data["startDate"].apply(
        lambda x: datetime.strptime(x, '%d-%m-%Y').strftime('%a'))
    #data["uploadstatus"] = "no"
    # data["startDate"].head(2)
    #while ("no" in data["uploadstatus"].values):
    
    grouped_user = data.groupby('userId')
    master(driver, grouped_user, unique_user)
