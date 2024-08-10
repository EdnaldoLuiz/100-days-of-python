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

    def verificar_palpite():
        valor = int(palpite.get())

        if valor == numero_secreto:
            resultado = "Parabéns! Você acertou o número."
        elif valor < numero_secreto:
            resultado = "Tente um número maior."
        else:
            resultado = "Tente um número menor."
        resultado_label.config(text=resultado)

    verificar = tk.Button(janela, text="Verificar", command=verificar_palpite)
    verificar.pack()
    resultado_label = tk.Label(janela, text="")
    resultado_label.pack()
    janela.mainloop()

if __name__ == "__main__":
    main()