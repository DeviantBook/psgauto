import telebot

bot = telebot.TeleBot("955868900:AAEQrEqu3UtgO9aqfmzMTFT7avCbJXMWuGA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, "Добрый день! Программисты PAL-GATE в ближайшее время запустят бота, для Вашего удобства!) Пока вы можете посетить сайт pal-gate.ru")

	bot.polling( none_stop = True )