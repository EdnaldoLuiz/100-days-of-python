from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'ChatBotSimples',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///chatbot.sqlite3'
)

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.portuguese')

print("Digite 'sair' para encerrar o chat.")
while True:
    user_input = input("Você: ")
    if user_input.lower() == 'sair':
        print("ChatBot: Até logo!")
        break

    response = chatbot.get_response(user_input)
    print(f"ChatBot: {response}")
