# Desafio 30

Trabalhando com logs e configurando um logger

## Explicação

### Ferramentas Utilizadas

- `logging`: Biblioteca padrão do Python para geração de logs.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `logging.basicConfig()`: Configura o logger.
- `logging.debug()`: Gera uma mensagem de log de nível DEBUG.
- `logging.info()`: Gera uma mensagem de log de nível INFO.
- `logging.warning()`: Gera uma mensagem de log de nível WARNING.

## Resultado

```py
import logging
import os

base_path = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_path, 'assets')
log_file = os.path.join(assets_dir, 'example.log')
utf8 = 'utf-8'

logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode='w', encoding=utf8)

logging.debug('Isso é uma mensagem de debug')
logging.info('Isso é uma mensagem de informação')
logging.warning('Isso é uma mensagem de aviso')