__author__ = 'anastasiiakorosteleva'
import requests
import re
from lxml import etree


url_start = "https://en.wikipedia.org/wiki/Gone_Maggie_Gone"
url_finish = "https://en.wikipedia.org/wiki/Theia_(planet)"
global_url = 'https://en.wikipedia.org'

def get_ref(ref):
    data = requests.get(ref).text
    parser = etree.HTMLParser()
    tree = etree.fromstring(data, parser)
    links = tree.xpath("//a/@href")
    results = re.findall("/wiki/[\w\(\)]+", str(links))
    return results

def func():
    for i in get_ref(url_start):
        if global_url+i == url_finish:
            return (url_start, global_url+i)
        else:
            for j in get_ref(global_url+i):
                if global_url+j == url_finish:
                    return (url_start, global_url+i, global_url+j)

result = []
result = func()
for i in result:
    print(i)
