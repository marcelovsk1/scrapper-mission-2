from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.facebook.com/events?source=46&action_history=null')
webpage = BeautifulSoup(page.content, 'html.parser')

print(webpage.prettify())

events = webpage.find_all('div', attrs={'class': 'Grid__GridStyled-sc-1l00ugd-0.bdoWSJ.grid'})

event_name = [i.find('h3', attrs={'id':'event-title'}).text for i in events ]

names = [x.find('a').get('title') for x in event_name]

print(names)
