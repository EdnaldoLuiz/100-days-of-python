import zipfile
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
file_1 = os.path.join(assets_dir, 'arquivo_1.txt')
file_2 = os.path.join(assets_dir, 'arquivo_2.txt')
zip_file = os.path.join(assets_dir, 'arquivo.zip')

os.makedirs(assets_dir, exist_ok=True)

def criar_zip_senha(arquivo_zip, arquivos, senha):
    """
    Cria um arquivo zip protegido por senha.
    """
    with zipfile.ZipFile(arquivo_zip, 'w') as zipado:
        for arquivo in arquivos:
            zipado.write(arquivo)
        zipado.setpassword(senha)

def verificar_zip_senha(arquivo_zip, senha):
    """
    Verifica se um arquivo zip está protegido por senha.
    """
    try:
        with zipfile.ZipFile(arquivo_zip, 'r') as zipado:
            zipado.extractall(pwd=senha)
            print(f"Arquivo {arquivo_zip} descompactado com sucesso!")
    except Exception as e:
        print(f"Erro ao descompactar {arquivo_zip}: {e}")

arquivo_zip = zip_file
arquivos = [file_1, file_2]
senha = b'senha'
criar_zip_senha(arquivo_zip, arquivos, senha)

verificar_zip_senha(arquivo_zip, senha)