import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from  credentials import credentials

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service("./chromedriver"),options=options)

driver.get('https://tr.linkedin.com/')
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="session_key"]').click()
time.sleep(1.5)
driver.find_element(By.XPATH,'//*[@id="session_key"]').send_keys(credentials()['username'])
time.sleep(1.2)


driver.find_element(By.XPATH, '//*[@id="session_password"]').click()
time.sleep(1.1)

driver.find_element(By.XPATH, '//*[@id="session_password"]').send_keys(credentials()['password'])
time.sleep(1.5)


driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/button').click()


# confirmation 

try:
    driver.find_element(By.XPATH,'//*[@id="ember26"]/button[1]').click()
except:
    pass

# search on search bar
driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input').send_keys('frontend developer')
driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input').send_keys(Keys.ENTER)
time.sleep(5)


# if the page is not navigated to jobs page directly click on jobs button
try:
    driver.find_element(By.XPATH,'//*[@id="search-reusables__filters-bar"]/ul/li[2]/button').click()
except:
    pass


# collect list of job posts
time.sleep(5)
ul = driver.find_element(By.CLASS_NAME,'scaffold-layout__list-container')
all_li = ul.find_elements(By.TAG_NAME,'li')
for count,li in enumerate(all_li):
    # job post link 
    try:
        if('ember' in li.get_attribute('id')):
            li.click()
            text = driver.find_element(By.ID,'job-details').text
            if(len(text) > 5):
                with open(f'{count}.txt','w') as f:
                    f.write(text)
            time.sleep(5)
    except:
        time.sleep(2)
        pass
        
    



time.sleep(5)


