import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

url = 'https://books.toscrape.com/'
driver.get(url)

driver.find_element(By.TAG_NAME, 'a')[54].text

result_dict = {'element_texts': element_texts}

result_json = json.dumps(result_dict, indent=2)

print(result_json)
driver.quit()
