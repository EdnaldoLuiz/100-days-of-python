# Desafio 91

Realizando análises de sentimentos com TextBlob

## Explicação

### Ferramentas Utilizadas

- `textblob`: Biblioteca para processamento de texto e análise de sentimentos.

### Funções Principais

- `TextBlob()`: Cria um objeto TextBlob a partir de um texto.
- `blob.sentiment`: Analisa o sentimento do texto.

## Resultado

```py
from textblob import TextBlob

texts = [
    "I love this product! It's absolutely amazing.",
    "This is the worst experience I've ever had.",
    "I'm not sure how I feel about this.",
    "It's okay, not great but not terrible either.",
    "Absolutely fantastic! Highly recommend it."
]

for text in texts:
    blob = TextBlob(text)
    sentiment = blob.sentiment
    print(f'Text: {text}')
    print(f'Sentiment: {sentiment}\n')