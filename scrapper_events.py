from bs4 import BeautifulSoup
import requests

page = requests.get('https://ra.co/events/ca/montreal')

webpage = BeautifulSoup(page.content, 'html.parser')

events = webpage.find_all('div', attrs={'class': 'Box-omzyfs-0.guLsXx'})

print(events)
