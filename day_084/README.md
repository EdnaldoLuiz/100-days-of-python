# Desafio 84

Trabalhando com paralelismo usando Dask para grandes volumes de dados

## Explicação

### Ferramentas Utilizadas

- `dask.dataframe`: Biblioteca para manipulação de grandes volumes de dados com paralelismo.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `dd.read_csv()`: Lê um arquivo CSV em um DataFrame Dask.
- `df.compute()`: Executa as operações de forma paralela e retorna um DataFrame Pandas.

## Resultado

```py
import os
import dask.dataframe as dd

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
arquivo = os.path.join(assets_dir, 'arquivo_100_linhas.csv')
arquivo_filtrado = os.path.join(assets_dir, 'resultado_filtrado.csv')

def main():
    # Lê o arquivo CSV em um DataFrame Dask
    df = dd.read_csv(arquivo)

    # Filtra os dados e arredonda os valores
    df_filtrado = df[df['Valor'] > 500].round(2)

    # Calcula a média da coluna 'Valor'
    media_valor = df_filtrado['Valor'].mean().compute()
    print(f"Média da coluna 'Valor': {media_valor.round(2)}")

    # Salva o DataFrame filtrado em um novo arquivo CSV
    df_filtrado.to_csv(arquivo_filtrado, single_file=True)

if __name__ == "__main__":
    main()