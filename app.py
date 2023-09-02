import telebot
import requests
import socket


import time

from settings import token
from descriptionlogger import log_error, log_info

from datetime import datetime



token_bot = token
bot = telebot.TeleBot(token)
id_chat = [1444648623, 1674676714]

@bot.message_handler(commands=['start'])
def startBotWorck(message):


    for i_id in id_chat:
        messeg = 'Бот запущен'
        url = f"https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={i_id}&text={messeg}"
        requests.get(url).json()

    def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return True
        except:
            return False

    while True:

        time.sleep(10)
        data_base = isOpen('194.87.232.22', 5432)
        if data_base is False:
            log_info.info(f'База данных отключена:  {datetime.now()}')
            messeg = 'База данных отключена'
            for i_id in id_chat:
                url = f"https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={i_id}&text={messeg}"
                requests.get(url).json()

        login_authorization = isOpen('194.87.232.22', 8080)

        if login_authorization is False:
            log_info.info(f'База данных отключена:  {datetime.now()}')
            messeg = 'Сервис login_authorization отключен'
            for i_id in id_chat:
                url = f"https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={i_id}&text={messeg}"
                requests.get(url).json()

        point_entry = isOpen('194.87.232.22', 8081)

        if point_entry is False:
            messeg = 'Сервис point_entry отключен'
            for i_id in id_chat:
                url = f"https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={i_id}&text={messeg}"
                requests.get(url).json()

        login_session = isOpen('194.87.232.22', 8082)

        if login_session is False:
            messeg = 'Сервис session отключен'
            for i_id in id_chat:
                url = f"https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={i_id}&text={messeg}"
                requests.get(url).json()

        login_data_file = isOpen('194.87.232.22', 8083)

        if login_data_file is False:
            messeg = 'Сервис data_file отключен'
            for i_id in id_chat:
                url = f"https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={i_id}&text={messeg}"
                requests.get(url).json()


bot.polling(none_stop=True, interval=0)
