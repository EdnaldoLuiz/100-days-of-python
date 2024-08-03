import tkinter as tk
from tkinter import ttk

def centralizar_janela(janela, largura, altura):
    """
    Centraliza a janela na tela.
    """
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

def main():
    """
    Função principal que cria a janela principal.
    """
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Exemplo de Interface Gráfica")
    largura = 400
    altura = 300
    janela.resizable(False, False)
    janela.configure(background="white")
    janela.attributes("-topmost", True)
    
    # Centraliza a janela
    centralizar_janela(janela, largura, altura)
    
    # Estilo
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12), background="white")
    style.configure("TButton", font=("Helvetica", 12))
    
    # Frame principal
    frame = ttk.Frame(janela, padding="10")
    frame.pack(expand=True)
    
    # Adiciona um rótulo de texto
    texto = ttk.Label(frame, text="Olá, mundo!")
    texto.pack(pady=10)
    
    # Adiciona uma entrada de texto
    entrada = ttk.Entry(frame, width=30)
    entrada.pack(pady=10)
    
    # Adiciona um botão
    botao = ttk.Button(frame, text="Clique aqui", command=lambda: print("Botão clicado!"))
    botao.pack(pady=10)
    
    # Inicia o loop de eventos da janela
    janela.mainloop()

if __name__ == "__main__":
    main()