import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

driver_path = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
