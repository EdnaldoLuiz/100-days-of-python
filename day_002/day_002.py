import datetime as dt
import locale

br_uft = 'pt_BR.UTF-8'
locale.setlocale(locale.LC_TIME, br_uft)

data_string = "25 de Dezembro de 2024"
data_formatada = dt.datetime.strptime(data_string, "%d de %B de %Y")

print(f"Tipo da primeira data: {type(data_string)}")
print(f"Tipo da segunda data: {type(data_formatada)}")

print(f"Data: {data_formatada}")