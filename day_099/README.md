# Desafio 99

Criando um modelo básico de NLP com spaCy

## Explicação

### Ferramentas Utilizadas

- `spacy`: Biblioteca para processamento de linguagem natural (NLP).

### Funções Principais

- `spacy.load()`: Carrega um modelo spaCy.
- `nlp()`: Processa um texto com o modelo carregado.
- `token.lemma_`: Obtém o lema de um token.
- `token.pos_`: Obtém a classe gramatical de um token.
- `doc.ents`: Obtém as entidades nomeadas no texto.

## Resultado

```python
import spacy

# Carrega o modelo spaCy para português
nlp = spacy.load("pt_core_news_sm")

def analisar_texto(texto):
    doc = nlp(texto)

    print("Tokens:")
    for token in doc:
        print(f"{token.text} (Lemma: {token.lemma_}, POS: {token.pos_})")

    print("\nEntidades Nomeadas:")
    for ent in doc.ents:
        print(f"{ent.text} (Label: {ent.label_})")

# Exemplo de uso
texto = "O Brasil é o maior país da América do Sul. São Paulo é uma grande cidade."
analisar_texto(texto)
```