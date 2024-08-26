# Desafio 73

Enviando requisições HTTP simultâneas com a biblioteca `aiohttp`

## Explicação

### Ferramentas Utilizadas

- `asyncio`: Biblioteca para programação assíncrona.
- `aiohttp`: Biblioteca para envio de requisições HTTP assíncronas.

### Funções Principais

- `async with aiohttp.ClientSession()`: Cria uma sessão HTTP assíncrona.
- `session.get(url)`: Envia uma requisição HTTP GET.
- `response.status`: Obtém o status da resposta.

## Resultado

```py
import asyncio
import aiohttp

async def requisicao(identificador):
    """
    Função executada por cada processo no pool.
    Envia uma requisição HTTP GET e exibe o status da resposta.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get') as response:
            status = response.status
            print(f"Requisição {identificador}: status {status}")
            return status

async def main():
    tarefas = [requisicao(i) for i in range(10)]
    await asyncio.gather(*tarefas)

if __name__ == '__main__':
    asyncio.run(main())