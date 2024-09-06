import os
import dask.dataframe as dd

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
arquivo = os.path.join(assets_dir, 'arquivo_100_linhas.csv')
arquivo_filtrado = os.path.join(assets_dir, 'resultado_filtrado.csv')

def main():
    df = dd.read_csv(arquivo)

    df_filtrado = df[df['Valor'] > 500].round(2)

    media_valor = df_filtrado['Valor'].mean().compute()
    print(f"Média da coluna 'Valor': {media_valor.round(2)}")

    df_filtrado.to_csv(arquivo_filtrado, single_file=True, index=False)

if __name__ == '__main__':
    main()