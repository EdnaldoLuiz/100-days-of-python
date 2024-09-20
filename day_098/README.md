# Desafio 98

Treinando um chatbot básico com ChatterBot

## Explicação

### Ferramentas Utilizadas

- `chatterbot`: Biblioteca para criação de chatbots.
- `chatterbot.trainers`: Módulo para treinamento de chatbots.

### Funções Principais

- `ChatBot()`: Cria um objeto chatbot.
- `ChatterBotCorpusTrainer()`: Treina o chatbot usando um corpus de dados.
- `trainer.train()`: Treina o chatbot com o corpus especificado.

## Resultado

```python
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Cria o chatbot
chatbot = ChatBot(
    'ChatBotSimples',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///chatbot.sqlite3'
)

# Treina o chatbot com o corpus em português
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.portuguese')

print("Digite 'sair' para encerrar o chat.")
while True:
    try:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            break
        response = chatbot.get_response(user_input)
        print(f"ChatBot: {response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
```