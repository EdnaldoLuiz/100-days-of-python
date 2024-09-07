# Desafio 85

Criando uma aplicação CLI interativa com a biblioteca Click

## Explicação

### Ferramentas Utilizadas

- `click`: Biblioteca para criação de interfaces de linha de comando (CLI) em Python.

### Funções Principais

- `@click.command()`: Define um comando CLI.
- `@click.option()`: Define uma opção para o comando CLI.
- `click.echo()`: Exibe uma mensagem na linha de comando.

## Resultado

```py
import click

@click.command()
@click.option('--name', prompt='Seu nome', help='O nome do usuário')
def main(name):
    click.echo(f'Olá, {name}!')

if __name__ == '__main__':
    main()