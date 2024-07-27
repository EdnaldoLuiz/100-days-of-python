import hashlib
import os

base_path = os.path.dirname(os.path.realpath(__file__))
assets_dir = os.path.join(base_path, "assets")
os.makedirs(assets_dir, exist_ok=True)
file_path = os.path.join(assets_dir, "usuarios.txt")

def cadastrar_usuario():
    """
    Função para cadastrar um novo usuário.
    """
    # Solicita o nome de usuário e a senha
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    # Realiza o hashing da senha
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    
    # Salva o nome de usuário e a senha hash em um arquivo
    with open(file_path, "a") as arquivo:
        arquivo.write(f"{nome_usuario} {senha_hash}\n")
    
    print("Usuário cadastrado com sucesso!")

def autenticar_usuario():
    """
    Função para autenticar um usuário.
    """
    # Solicita o nome de usuário e a senha
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    # Realiza o hashing da senha
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    
    # Verifica se o nome de usuário e a senha hash estão no arquivo
    with open(file_path, "r") as arquivo:
        for linha in arquivo:
            usuario, senha_salva = linha.strip().split()
            if usuario == nome_usuario and senha_salva == senha_hash:
                print("Usuário autenticado com sucesso!")
                return
    
    print("Usuário ou senha incorretos!")

def main():
    """
    Função principal do programa.
    """
    while True:
        print("\n1 - Cadastrar usuário")
        print("2 - Autenticar usuário")
        print("3 - Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            autenticar_usuario()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
