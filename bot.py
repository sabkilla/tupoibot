import pyowm
import telebot

owm = pyowm.OWM('01ae8be92647ab80f335b8ec0b2c1fb7', language = "ru")
bot = telebot.TeleBot("1408617044:AAHKbOwI-r1gEtkj-f-v7V2L2PJizxXfiJs")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас примерно " + str(temp) + "\n\n"

	if temp < 8:
		answer += "Сейчас очень холодно, оденься теплее"
	elif temp <15:
		answer += "Оденься потеплее"
	else:
		answer += "Температура нормальное, одевайся как хочешь"


	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
