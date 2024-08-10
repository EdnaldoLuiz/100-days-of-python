# Desafio 57

Construindo um simples jogo de adivinhação com interface gráfica

## Explicação

### Ferramentas Utilizadas

- `tkinter`: Biblioteca padrão do Python para criação de interfaces gráficas.
- `random.randint()`: Gera um número inteiro aleatório.

### Funções Principais

- `tk.Tk()`: Cria a janela principal da aplicação.
- `janela.geometry()`: Define o tamanho da janela.
- `tk.Label()`: Cria um rótulo de texto.
- `tk.Entry()`: Cria um campo de entrada de texto.
- `tk.Button()`: Cria um botão.

## Resultado

```py
import tkinter as tk
from random import randint

def main():
    janela = tk.Tk()
    janela.title("Jogo de Adivinhação")
    janela.geometry("400x200")

    instrucoes = tk.Label(janela, text="Adivinhe um número entre 1 e 100")
    instrucoes.pack()

    numero_secreto = randint(1, 100)
    palpite = tk.StringVar()

    entrada = tk.Entry(janela, textvariable=palpite)
    entrada.pack()

    resultado = tk.Label(janela, text="")
    resultado.pack()

    def verificar_palpite():
        try:
            palpite_usuario = int(palpite.get())
            if palpite_usuario < numero_secreto:
                resultado.config(text="Muito baixo!")
            elif palpite_usuario > numero_secreto:
                resultado.config(text="Muito alto!")
            else:
                resultado.config(text="Parabéns! Você acertou!")
        except ValueError:
            resultado.config(text="Por favor, insira um número válido.")

    botao = tk.Button(janela, text="Verificar", command=verificar_palpite)
    botao.pack()

    janela.mainloop()

if __name__ == "__main__":
    main()