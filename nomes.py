import requests
from bs4 import BeautifulSoup

url = 'https://super.abril.com.br/especiais/a-origem-dos-50-sobrenomes-mais-comuns-do-brasil/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


content = soup.find_all('h3')

tam = len(content)
ls_nomes = list()

for a in range(0, tam):

    ls_nomes.append(content[a].text.lower())

for a in range(0, len(ls_nomes)):
    print(ls_nomes[a])