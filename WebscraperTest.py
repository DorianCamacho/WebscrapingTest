from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.common.by import By

SITE = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

options = Options()
options.add_argument('disable-infobars')
options.add_argument('--incognito')
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)
driver.get(SITE)

prices = driver.find_elements(By.TAG_NAME,"h4")
descriptions = driver.find_elements(By.TAG_NAME,"p")
titles = driver.find_elements(By.TAG_NAME,"a")
links = driver.find_elements(By.TAG_NAME,"a")

priceList = []
linkList = []
titleList = []
descList = []

for price in prices:
    if price.get_attribute('class') == "pull-right price":
        priceList.append(price.text)

for desc in descriptions:
    if desc.get_attribute('class') == "description":
        descList.append(desc.text)

for title in titles:
    if title.get_attribute('class') == "title":
        titleList.append(title.get_attribute('title'))
        linkList.append(title.get_attribute('href'))

data = {
    "Name": titleList,
    "Description": descList,
    "Price": priceList,
    "Links": linkList
    }

Test = pd.DataFrame(data)

Test.to_csv('WebscraperTest.csv', index=False)
Test.to_json("WebcraperTest.json", indent=2, orient='records')