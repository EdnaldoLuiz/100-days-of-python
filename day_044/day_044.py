import pytz
import datetime

fuso_horario_sp = pytz.timezone("America/Sao_Paulo")

fuso_horario_ny = pytz.timezone("America/New_York")

fuso_horario_london = pytz.timezone("Europe/London")

current_utc_time = datetime.datetime.now(datetime.timezone.utc)
print("UTC Time: ", current_utc_time)

current_sp_time = current_utc_time.astimezone(fuso_horario_sp)
print("São Paulo Time: ", current_sp_time)