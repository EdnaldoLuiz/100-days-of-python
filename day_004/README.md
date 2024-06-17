# Desafio 4

Utilizando `asyncio` para criar funções assíncronas

## Explicação

### Ferramentas Utilizadas

- `asyncio`: Biblioteca padrão do Python para escrever código assíncrono.

### Funções Principais

- `asyncio.sleep()`: Suspende a execução da corrotina por um número especificado de segundos.
- `async def`: Define uma função assíncrona.
- `await`: Espera a conclusão de uma corrotina.
- `asyncio.run()`: Executa a função principal assíncrona.

## Resultado

```py
import asyncio

async def cumprimentar():
    print('Olá!')
    await asyncio.sleep(1)
    print('Como vai você?')

async def main():
    await cumprimentar()

asyncio.run(main())