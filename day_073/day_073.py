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
        

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    
    numero_de_requisicoes = 4
    tarefas = [requisicao(i) for i in range(numero_de_requisicoes)]
    print(f"Enviando {numero_de_requisicoes} requisições HTTP...")
    resultados = loop.run_until_complete(asyncio.gather(*tarefas))
    
    print(f"Resultados finais: {resultados}")