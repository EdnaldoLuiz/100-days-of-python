# Desafio 64

Trabalhando com tarefas agendadas usando a biblioteca `schedule`

## Explicação

### Ferramentas Utilizadas

- `schedule`: Biblioteca para agendamento de tarefas em Python.
- `time`: Biblioteca padrão do Python para manipulação de tempo.

### Funções Principais

- `schedule.every(intervalo).unidade.do(funcao)`: Agenda uma tarefa para ser executada em um intervalo específico.
- `schedule.run_pending()`: Executa todas as tarefas agendadas que estão pendentes.
- `time.sleep(segundos)`: Suspende a execução do programa pelo número de segundos especificado.

## Resultado

```py
import schedule
import time

def tarefa_agendada():
    print("Executando tarefa agendada...")
    print("Tarefa agendada executada com sucesso!")

# Agenda a tarefa para ser executada a cada 5 segundos
schedule.every(5).seconds.do(tarefa_agendada)

while True:
    schedule.run_pending()
    time.sleep(1)