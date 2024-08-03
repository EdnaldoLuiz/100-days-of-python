# Desafio 50

Criando uma interface gráfica simples com `tkinter`

## Explicação

### Ferramentas Utilizadas

- `tkinter`: Biblioteca padrão do Python para criação de interfaces gráficas.
- `ttk`: Módulo do `tkinter` para widgets temáticos.

### Funções Principais

- `tk.Tk()`: Cria a janela principal da aplicação.
- `janela.geometry()`: Define o tamanho e a posição da janela.
- `janela.winfo_screenwidth()`: Retorna a largura da tela.
- `janela.winfo_screenheight()`: Retorna a altura da tela.

## Resultado

```py
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
    janela = tk.Tk()
    janela.title("Interface Gráfica Simples")
    centralizar_janela(janela, 300, 200)

    label = ttk.Label(janela, text="Olá, mundo!")
    label.pack(pady=20)

    botao = ttk.Button(janela, text="Clique aqui", command=lambda: print("Botão clicado!"))
    botao.pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    main()