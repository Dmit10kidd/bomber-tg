import telebot
import os
import config
import subprocess
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def privetctive(message):
	sent = bot.send_message(message.chat.id, "Здравствуйте, какой номер телефона?")
	bot.register_next_step_handler(sent, Nomer)


def Nomer(message):
	doc = open('file.txt', 'w')
	doc.write("{nomer}\n".format(nomer=message.text))
	doc.close()
	sent2 = bot.send_message(message.chat.id, "Сколько раз отправить?")

@bot.message_handler(content_types=['text'])
def bomber(message):	
	doc = open('file2.txt', 'w')
	doc.write("{count}\n".format(count=message.text))
	p = subprocess.Popen(bombom, shell=True)


bombom= 'python bomber.py'


if __name__ == '__main__':
     bot.polling()
