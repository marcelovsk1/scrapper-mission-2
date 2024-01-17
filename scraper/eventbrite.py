from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.eventbrite.com/d/canada--montreal/events/')
webpage = BeautifulSoup(page.content, 'html.parser')

events = webpage.find_all('div', attrs={'class': 'Stack_root__1ksk7'})

event_names = [event.find('h2').text for event in events]
event_dates = [event.find('p').text.strip() for event in events]

for name, date in zip(event_names, event_dates):
    print(f"{name}")
    print(f"{date}")
    print("=" * 100)

# JSON
# import json
# from bs4 import BeautifulSoup
# import requests

# page = requests.get('https://www.eventbrite.com/d/canada--montreal/events/')
# webpage = BeautifulSoup(page.content, 'html.parser')

# events = webpage.find_all('div', attrs={'class': 'Stack_root__1ksk7'})

# event_names = [event.find('h2').text for event in events]

# data = {'event_names': event_names}

# # Convert to JSON
# json_data = json.dumps(data, ensure_ascii=False, indent=2)

# print(json_data)
