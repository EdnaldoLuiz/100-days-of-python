# Desafio 58

Analisando texto e realizando contagem de palavras com NLTK

## Explicação

### Ferramentas Utilizadas

- `nltk`: Biblioteca para processamento de linguagem natural.
- `word_tokenize()`: Função para tokenização de palavras.
- `stopwords`: Lista de palavras comuns que são filtradas.

### Funções Principais

- `nltk.download()`: Baixa os recursos necessários do NLTK.
- `word_tokenize(texto)`: Tokeniza o texto em palavras.
- `stopwords.words('portuguese')`: Obtém a lista de stopwords em português.
- `nltk.FreqDist()`: Calcula a frequência das palavras.

## Resultado

```py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('portuguese'))
texto = "O Brasil é um país tropical, com muitas praias e florestas. A Amazônia é a maior floresta tropical do mundo."

tokens = word_tokenize(texto)
tokens_sem_stopwords = [token for token in tokens if token.lower() not in stop_words]

frequencia = nltk.FreqDist(tokens_sem_stopwords)
print(frequencia.most_common(5))