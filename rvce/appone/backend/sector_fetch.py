from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions
import time
import csv
import os

dirname=os.path.dirname(__file__)
options = ChromeOptions()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
PATH="./chromedriver.exe"
options=ChromeOptions()
    #options.headless=True
ser=Service(PATH)

def fetch_sector():
    
    Wd=webdriver.Chrome(service=ser,options=options)
    Wd.get(f"https://ngodarpan.gov.in/index.php/search/")
    Wd.maximize_window()
    time.sleep(5)
    
    Wd.find_element(By.XPATH, '//*[@id="search_form_container"]/div[3]/div/span/span[1]').click()
    
    #Wd.find_elements(By.XPATH, '//li[@"class=select2-results__option"]')
    sectornames = [i.text for i in Wd.find_elements(By.XPATH, '//*[@class="select2-results__option"]')]
    
    #print(sectornames)

    with open(f"sectors.csv","w") as fp:
     writerp=csv.writer(fp)
     writerp.writerow(sectornames)

fetch_sector()


