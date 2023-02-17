from bs4 import BeautifulSoup
import requests
import json

url = "http://kitahamagmcojp.local/contact/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

array = []

for ele in soup.find('body').find_all(['input', 'textarea', 'select']):
    if 'type' in ele.attrs and ele.attrs['type'] == 'hidden':
        continue

    array.append(dict({'tag_name': ele.name}, **ele.attrs))
    
with open('output.json', 'w', encoding='UTF-8') as f:
    json.dump(array, f, indent=2, ensure_ascii=False)