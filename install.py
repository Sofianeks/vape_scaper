import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.vapeshows.com/events')

soup = BeautifulSoup(res.text, 'html.parser')

events = soup.find_all(class_='events')

for event in events:
    name = event.find('h2').get_text()
print(event)