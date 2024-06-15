# Desafio 2

Formatando datas e horas usando `datetime`

## Explicação

### Ferramentas Utilizadas

- `datetime`: Biblioteca padrão do Python para manipulação de datas e horas.
- `locale`: Biblioteca padrão do Python para configuração de localidade.

### Funções Principais

- `locale.setlocale()`: Configura a localidade para formatação de datas.
- `datetime.strptime()`: Converte uma string de data em um objeto `datetime`.

## Resultado

```py
import datetime as dt
import locale

br_utf = 'pt_BR.UTF-8'
locale.setlocale(locale.LC_TIME, br_utf)

data_string = "25 de Dezembro de 2024"
data_formatada = dt.datetime.strptime(data_string, "%d de %B de %Y")

print(f"Tipo da primeira data: {type(data_string)}")
print(f"Tipo da segunda data: {type(data_formatada)}")
print(f"Data: {data_formatada}")