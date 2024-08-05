# Desafio 52

Criando um bot simples para Telegram

## Explicação

### Ferramentas Utilizadas

- `telebot`: Biblioteca para criar bots no Telegram.

### Funções Principais

- `TeleBot(token)`: Cria um objeto bot.
- `@bot.message_handler(commands=['comando'])`: Define um manipulador para um comando específico.
- `bot.reply_to(message, texto)`: Responde a uma mensagem.
- `@bot.message_handler(func=lambda message: True)`: Define um manipulador para todas as mensagens.

## Resultado

```py
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

if __name__ == "__main__":
    bot.polling()