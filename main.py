import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('45d4a007abaa22e657aee915f5dd51ce', config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot("6961161412:AAFeE5kCKQUis3_uKf2MPylzBkpvhb2JGi4")


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = round(w.temperature('celsius')['temp'])
    answer = 'В городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
    answer += 'Температура воздуха ' + str(temp) + ' °C'

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
