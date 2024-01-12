import requests
from bs4 import BeautifulSoup

try:
    url = 'https://www.unian.ua/'

    response = requests.get(url).text

    soup = BeautifulSoup(response, 'html.parser')

    
    article = soup.find('li', class_='newsfeed__item')
    article_strong = soup.find('li', class_='newsfeed__item strong')
    
    article_id = article["id"]
    article_strong_id = article_strong["id"]
    
    
    title = article.a.text
    link = article.a['href']
    title_strong = article_strong.a.text
    link_strong = article_strong.a['href']

    with open('post_all.txt', 'w', encoding='utf-8') as file:
        file.write(f"{title}\n{link}")
        file.write(f"\n{title_strong}\n{link_strong}")
        
except Exception as e:
    print(f"{e}")
