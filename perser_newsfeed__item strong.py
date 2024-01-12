import requests
from bs4 import BeautifulSoup

try:
    url = 'https://www.unian.ua/'

    response = requests.get(url).text

    soup = BeautifulSoup(response, 'html.parser')

    
    article = soup.find('li', class_='newsfeed__item strong')
    
    
    title = article.a.text
    link = 'https://www.unian.ua/' + article.a['href']

    with open('post_strong.txt', 'w', encoding='utf-8') as file:
        file.write(f"{title}\n{link}")
        
except Exception as e:
    print(f"{e}")
