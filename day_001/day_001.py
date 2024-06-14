import os

def criar_pastas_e_arquivos():

    diretorio_atual = os.getcwd()
    print(f"Criando pastas no diretório: {diretorio_atual}")

    for i in range(1, 101):

        nome_pasta = f"day_{i:03d}"
        caminho_pasta = os.path.join(diretorio_atual, nome_pasta)

        os.makedirs(caminho_pasta, exist_ok=True)

        script_nome = f"{nome_pasta}.py"
        caminho_script = os.path.join(caminho_pasta, script_nome)
        with open(caminho_script, 'w') as script:
            script.write(f"# Script para {nome_pasta}\n")
            script.write(f"print('Executando {script_nome}')\n")

        caminho_readme = os.path.join(caminho_pasta, "README.md")
        with open(caminho_readme, 'w') as readme:
            readme.write(f"# {nome_pasta}\n")
            readme.write("Este é o README para esta pasta.\n")

        print(f"Pasta, script e README criados em: {caminho_pasta}")

if __name__ == "__main__":
    criar_pastas_e_arquivos()
