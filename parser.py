import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.s-vfu.ru/universitet/rukovodstvo-i-struktura/instituty/imi/Vremennoe_raspisanie_IMI_na_1_2020-2021/'

r = requests.get(url)
html = BS(r.content, 'html.parser')

for i in (html.select('a')):
    if 'ИМИ Расписание учебных занятий на 1 полугодие ' in str(i):
        print(i)

