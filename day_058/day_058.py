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
print(frequencia['Brasil'])