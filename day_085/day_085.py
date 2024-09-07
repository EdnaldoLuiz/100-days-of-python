import click

@click.command()
@click.option('--name', prompt='Seu nome', help='O nome do usuário')
def main(name):
    click.echo(f'Olá, {name}!')

if __name__ == '__main__':
    main()