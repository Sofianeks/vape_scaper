import requests
from bs4 import BeautifulSoup
from sty import fg, rs, RgbFg, bg
res = requests.get('https://www.vapeshows.com/events')

soup = BeautifulSoup(res.text, 'html.parser')
events = soup.select('.event')

for event in events:
    event_name = event.find('h2').get_text()
    event_place = event.select('p')[0].text.encode('utf-8')
    event_date = event.select('p')[1].text
    event_image = event.find('img')['src'].replace('//','https://')

    event_adresse = event.find('a')['href'].replace('/events/','https://www.vapeshows.com/events/')
    res1 = requests.get(event_adresse)
    soup1 = BeautifulSoup(res1.text, 'html.parser')
    event_detail_place = soup1.select('.event-content-column > h3')[0].get_text()
    
    socials = soup1.select('.event-content-column > .event-social')
    for social in socials:
        event_detail_social = social.select('a')
        if len(event_detail_social)>0:
            ev_detail_social_link_1 = event_detail_social[0]['href']
        else: ev_detail_social_link_1 =('nope!')
        if len(event_detail_social)>1:
            ev_detail_social_link_2 = event_detail_social[1]['href']
        else: ev_detail_social_link_2 =('nope!_again')
    
    
    
    
    p_ev_detail_social_link_2 = bg.li_magenta + fg.black + ev_detail_social_link_2 + fg.rs + bg.rs
    p_ev_detail_social_link_1 = bg.blue + ev_detail_social_link_1 + bg.rs
    p_event_name = fg.red + event_name + fg.rs
    print(p_event_name)
    print(event_place)
    print(event_date)
    print(event_image)
    print(event_adresse)
    print(event_detail_place)
    print(p_ev_detail_social_link_1, p_ev_detail_social_link_2)
