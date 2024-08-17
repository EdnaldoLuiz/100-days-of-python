import schedule
import time

def tarefa_agendada():
    print("Executando tarefa agendada...")
    print("Tarefa agendada executada com sucesso!")

schedule.every(5).seconds.do(tarefa_agendada)

while True:
    schedule.run_pending()
    time.sleep(1)