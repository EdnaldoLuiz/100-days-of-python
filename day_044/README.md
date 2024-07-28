# Desafio 44

Trabalhando com data e hora em diferentes fusos horários

## Explicação

### Ferramentas Utilizadas

- `pytz`: Biblioteca para fusos horários.
- `datetime`: Biblioteca padrão do Python para manipulação de datas e horas.

### Funções Principais

- `pytz.timezone()`: Cria um objeto de fuso horário.
- `datetime.datetime.now()`: Obtém a data e hora atual.
- `datetime.timezone.utc`: Representa o fuso horário UTC.
- `astimezone()`: Converte a data e hora para outro fuso horário.

## Resultado

```py
import pytz
import datetime

fuso_horario_sp = pytz.timezone("America/Sao_Paulo")
fuso_horario_ny = pytz.timezone("America/New_York")
fuso_horario_london = pytz.timezone("Europe/London")

current_utc_time = datetime.datetime.now(datetime.timezone.utc)
print("UTC Time: ", current_utc_time)

current_sp_time = current_utc_time.astimezone(fuso_horario_sp)
print("São Paulo Time: ", current_sp_time)

current_ny_time = current_utc_time.astimezone(fuso_horario_ny)
print("New York Time: ", current_ny_time)

current_london_time = current_utc_time.astimezone(fuso_horario_london)
print("London Time: ", current_london_time)