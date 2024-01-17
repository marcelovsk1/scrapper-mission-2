# from bs4 import BeautifulSoup
# import requests


# page = requests.get('https://www.eventbrite.com/d/canada--montreal/events/')
# webpage = BeautifulSoup(page.content, 'html.parser')

# events = webpage.find_all('div', attrs={'class': 'Stack_root__1ksk7'})

# for event in events:
#     event_name = event.find('h2').text
#     event_date = event.find('p').text.strip()
#     event_location = event.find('p', class_='Typography_root__487rx #585163 Typography_body-md__487rx event-card__clamp-line--one Typography_align-match-parent__487rx').text.strip()

#     print(f"{event_name}")
#     print(f"{event_date}")
#     print(f"{event_location}")
#     print("=" * 100)



# # JSON
import json
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.eventbrite.com/d/canada--montreal/events/')
webpage = BeautifulSoup(page.content, 'html.parser')

events = webpage.find_all('div', attrs={'class': 'Stack_root__1ksk7'})

event_list = []

for event in events:
    event_name = event.find('h2').text
    event_date = event.find('p').text.strip()

    # Verificar se o elemento 'p' com a classe desejada existe
    event_location_elem = event.find('p', class_='Typography_root__487rx #585163 Typography_body-md__487rx event-card__clamp-line--one Typography_align-match-parent__487rx')
    event_location = event_location_elem.text.strip() if event_location_elem else None

    event_dict = {
        'event_name': event_name,
        'event_date': event_date,
        'event_location': event_location
    }

    event_list.append(event_dict)

# Converter a lista de dicionários para uma string JSON
json_data = json.dumps(event_list, indent=2)

# Imprimir a string JSON
print(json_data)
