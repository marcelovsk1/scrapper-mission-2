from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.eventbrite.com/d/canada--montreal/events/')
webpage = BeautifulSoup(page.content, 'html.parser')

events = webpage.find_all('div', attrs={'class': 'Stack_root__1ksk7'})

for event in events:
    event_name = event.find('h2').text
    event_date = event.find('p').text.strip()
    event_location = event.find('p', class_='Typography_root__487rx #585163 Typography_body-md__487rx event-card__clamp-line--one Typography_align-match-parent__487rx').text.strip()

    print(f"{event_name}")
    print(f"{event_date}")
    print(f"{event_location}")
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
