# Desafio 90

Implementando um crawler distribuído com Scrapy

## Explicação

### Ferramentas Utilizadas

- `scrapy`: Biblioteca para criação de crawlers.
- `scrapy_redis`: Extensão para Scrapy que permite a distribuição de crawlers usando Redis.

### Funções Principais

- `RedisSpider`: Classe base para criação de spiders distribuídos.
- `parse()`: Método para processar a resposta da requisição.

## Resultado

```python
import scrapy
from scrapy_redis.spiders import RedisSpider

class ExampleSpider(RedisSpider):
    name = 'example'
    redis_key = 'example:start_urls'

    def parse(self, response):
        title = response.xpath('//title/text()').get()
        yield {'title': title}
```