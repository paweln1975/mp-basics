"""
XML parsing library training
>>> import sys; sys.tracebacklimit = 0
>>> x = xml_read_file('my_file_1.xml')
>>> print(x)
Gladiator
>>> families = '<?xml version="1.0" encoding="UTF-8"?> <families><family name="Swan-Dwyer"><parent name="Charlie"/><parent name="Renee"/><daughter name="Isabella"/></family><family name="Cullen-Hale"><parent name="Carlisle"/><parent name="Esme"/><daughter name="Alice"/><son name="Emmet"/><daughter name="Rosalie"/><son name="Jasper"/><son name="Edward"/></family></families>'
>>> y = extract_parent_tag(families, 'son')
>>> print(y)
family
"""

import requests
from bs4 import BeautifulSoup

def read_xml_from_url(url):
    r = requests.get('https://www.newsinlevels.com/products/albino-tortoise-level-1/')
    print(r.status_code)  # 200
    soup = BeautifulSoup(r.content, 'html.parser')

    p1 = soup.find('title')
    # print(p1)
    # print(soup.head.title.text)

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


def xml_read_file(file_name):
    file = open(file_name, "r").read()
    soup = BeautifulSoup(file, 'xml')
    tag1 = soup.find("title")
    return tag1.text


def extract_parent_tag(xml_content: str, tag_name: str) -> str:
    soup = BeautifulSoup(xml_content, 'xml')
    tag1 = soup.find(tag_name)
    return tag1.parent.name