import telebot

bot = telebot.TeleBot("SEU_TOKEN_AQUI")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Olá! Eu sou um bot simples para Telegram.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Você pode usar os comandos /start e /help.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()