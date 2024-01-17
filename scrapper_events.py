from bs4 import BeautifulSoup
import requests

page = requests.get('https://ra.co/events/ca/montreal')

webpage = BeautifulSoup(page.content, 'html.parser')
