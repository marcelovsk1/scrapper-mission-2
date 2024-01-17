from bs4 import BeautifulSoup
import requests


page = requests.get('https://www.eventbrite.com/d/canada--montreal/events/')
webpage = BeautifulSoup(page.content, 'html.parser')

events = webpage.find_all('div', attrs={'class': 'Stack_root__1ksk7'})

for event in events:
    event_name = event.find('h2').text
    event_date = event.find('p').text.strip()
    event_location = event.find('p', class_='Typography_root__487rx #585163 Typography_body-md__487rx event-card__clamp-line--one Typography_align-match-parent__487rx').text.strip()
    event_image = event.find('a', class_='event-card-link')

    image_url = event_image['href'] if event_image else None

    print(f"{event_name}")
    print(f"{event_date}")
    print(f"{event_location}")
    print(f"Image URL: {image_url}")
    print("=" * 100)


# # JSON
# import json
# from bs4 import BeautifulSoup
# import requests

# page = requests.get('https://www.eventbrite.com/d/canada--montreal/events/')
# webpage = BeautifulSoup(page.content, 'html.parser')

# events = webpage.find_all('div', attrs={'class': 'Stack_root__1ksk7'})

# event_list = []

# for event in events:
#     event_name = event.find('h2').text
#     event_date = event.find('p').text.strip()

# # Check if the element 'p' with the desired class exists
#     event_location_elem = event.find('p', class_='Typography_root__487rx #585163 Typography_body-md__487rx event-card__clamp-line--one Typography_align-match-parent__487rx')
#     event_location = event_location_elem.text.strip() if event_location_elem else None

#     event_dict = {
#         'event_name': event_name,
#         'event_date': event_date,
#         'event_location': event_location
#     }

#     event_list.append(event_dict)

# # Convert the list of dictionaries to a JSON string
# json_data = json.dumps(event_list, indent=2)

# # Print the JSON string
# print(json_data)
