import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('TOKEN', config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = round(w.temperature('celsius')['temp'])
    answer = 'В городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
    answer += 'Температура воздуха ' + str(temp) + ' °C'

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
