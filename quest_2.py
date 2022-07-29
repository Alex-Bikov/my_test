from bs4 import BeautifulSoup
import requests
import re

def chek(my_str):
    flag = True
    if len(my_str) <= 1:
        flag = False
    return flag

url = 'https://ru.wikipedia.org'
first_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
pets = list()
my_p = dict()
my_req = requests.get(first_url)
soup = BeautifulSoup(my_req.text, "html.parser")
pets = soup.findAll(class_='mw-category-group')
x = soup.findAll(class_='mw-category-generated')
pattern = r"href=(.*?)Следующая"
y = re.findall(pattern, my_req.text)
pages = 'pages'
for i in pets[2].text .split('\n'):
    if (chek(i)):
        if i[0] in my_p:
            my_p[i[0]] += 1
        else:
            my_p[i[0]] = 1
print(y[0])
z = '/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&amp%3Bpagefrom=%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B9+%D0%BC%D1%83%D1%80%D0%B0%D0%B2%D0%B5%D0%B9-%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%BE%D0%B9&pagefrom=%D0%90%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%B4%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D1%80%D1%8B%D0%BB%D0%B0%D1%8F+%D0%B0%D0%BA%D1%83%D0%BB%D0%B0#mw-pages'
print(z in my_req)










