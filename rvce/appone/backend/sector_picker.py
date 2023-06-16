from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

dirname=os.path.dirname(__file__)
options = ChromeOptions()
#options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
PATH="./chromedriver.exe"
options=ChromeOptions()
options.headless=True
ser=Service(PATH)

def getNGOs(category):
    Wd=webdriver.Chrome(service=ser,options=options)
    Wd.get("https://ngodarpan.gov.in/index.php/search/")
    Wd.maximize_window()
    time.sleep(3)

    Wd.find_element(By.XPATH, '//*[@id="select2-state_search_search-container"]').click()
    state = Wd.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
    state.send_keys("KARNATAKA")
    state.send_keys(Keys.RETURN)

    time.sleep(1)
    Wd.find_element(By.XPATH, '//*[@id="select2-district_search-container"]').click()
    district = Wd.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
    district.send_keys("Bangalore")
    district.send_keys(Keys.RETURN)
    time.sleep(1)

    Wd.find_element(By.XPATH, '//*[@id="search_form_container"]/div[3]/div/span/span[1]').click()
    sector = Wd.find_element(By.XPATH, '//*[@id="search_form_container"]/div[3]/div/span/span[1]/span/ul/li/input')
    sector.send_keys(category)
    sector.send_keys(Keys.RETURN)
    time.sleep(1)
    
    Wd.find_element(By.XPATH, '//*[@id="search_form_container"]/div[7]/div[1]/input').click()
    time.sleep(1)

    l=[]
    k=[]
    for i in range(1,6):
        k=[]
        t = Wd.find_element(By.XPATH, f'//*[@id="example"]/tbody/tr[{i}]/td[2]/a').text
        k.append(t)
        t = Wd.find_element(By.XPATH, f'//*[@id="example"]/tbody/tr[{i}]/td[3]').text
        k.append(t)
        l.append(k)
    return l

getNGOs(category="Agriculture")



