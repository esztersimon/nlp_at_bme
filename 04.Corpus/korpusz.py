# weboldalak letoltese es file-ba mentese
import urllib.request

urllib.request.urlretrieve('http://python.org/', 'website.html')


# weboldalak bejarasa, feldolgozasa
from bs4 import BeautifulSoup

# stringből
html = '''
<html>
    <head>
        <title>BeautifulSoup példa</title>
    </head>
    <body>
        <h1>Korpuszépítés</h1>
        <p>Lórum ipse nem kodik, ha kodik, már nem siánság többé. 
        Illírnek lengi hangás a botós és a nyalmas burniák 
        vencshez való lászovátomát az állott gyávatokban? </p>
        <ul>
            <li>Listaelem 1</li>
            <li>Listaelem 2</li>
            <li>Listaelem 3</li>
        </ul>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(type(soup), '\n\n')   # a leves típusa
print(soup.prettify())      # tagek rendezése, formázás

# fájlból

soup = BeautifulSoup(open('website.html', encoding='utf-8'), 'html.parser')
print(soup.prettify())


# tagek

links = soup.find_all('a')  # .find_all() kigyűjti az oldalról az összes paraméterként átadott taget
for link in links[:10]:
    print(link.get('href')) # .get() egy attribútum értékét adja vissza


links = soup.find_all('a', 'word')  # csak a "word" értékkel rendelkező a tagek kigyűjtése 
for link in links:
    print(link.get_text())

# szöveg

print(links[4])
print()
print(links[4].get_text())  # .get_text() kinyeri az adott tagen belüli (összes) szöveget



