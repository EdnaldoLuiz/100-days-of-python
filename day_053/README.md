# Desafio 53

Trabalhando com regex para encontrar e substituir padrões em arquivos

## Explicação

### Ferramentas Utilizadas

- `re`: Biblioteca padrão do Python para operações com expressões regulares.

### Funções Principais

- `re.findall(padrao, texto)`: Encontra todas as ocorrências do padrão no texto.
- `re.sub(padrao, substituicao, texto)`: Substitui todas as ocorrências do padrão no texto pela substituição.

## Resultado

```py
import re

padrao = r"\b\d{3}\b"

texto = "123 456 789 101112 131415 161718 192021"

# Encontrar todas as ocorrências do padrão no texto
resultados = re.findall(padrao, texto)
print(resultados)

# Substituir todas as ocorrências do padrão no texto pela substituição
substituicao = "XXX"
resultado = re.sub(padrao, substituicao, texto)
print(resultado)