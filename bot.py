import telebot
import requests
import time
from bs4 import BeautifulSoup

token = "6821307147:AAE5xXy_y4QCoe2JNf22jLAEQ6nm54xrT4I"
id_channel = "-1002034641376"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def parser(message):
    
    if message.text == "start":
        while True:    
            
            url = 'https://www.unian.ua/'

            response = requests.get(url).text

            soup = BeautifulSoup(response, 'html.parser')

            
            article = soup.find('li', class_='newsfeed__item')
            article_strong = soup.find('li', class_='newsfeed__item strong')
            
            
            title = article.a.text
            link = article.a['href']
            title_strong = article_strong.a.text
            link_strong = article_strong.a['href']
        
            bot.send_message(id_channel, f"{title}\n{link}")
            
            time.sleep(600)
    
    

bot.polling()