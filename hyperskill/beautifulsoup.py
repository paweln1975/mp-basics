import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.newsinlevels.com/products/albino-tortoise-level-1/')
print(r.status_code)  # 200
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())
p1 = soup.find('title')
print(p1)
print(soup.head.title.text)

a = soup.find_all('a')
for i in a:
    print(i.get('href'))


letter = 'S'
url = 'http://web.archive.org/web/20201201053628/https://www.who.int/health-topics'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
a_list = []
a = soup.find_all('a')
for i in a:
    if i.text.startswith(letter):
        a_list.append(i.text)

# clear
first_topic = 'Schistosomiasis'
last_topic = 'Sustainable Development Goals'

topic_list = []
add = False
for t in a_list:
    if not add:
        add = (t == first_topic)
    if add:
        topic_list.append(t)
        if t == last_topic:
            add = False

print(topic_list)
