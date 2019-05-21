import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.vapeshows.com/events')

soup = BeautifulSoup(res.text, 'html.parser')

with open('res') as evs:
    events = soup.find_all(class_='events')
    for event in events:
        name = events.find('h2').get_text()
    print(events)