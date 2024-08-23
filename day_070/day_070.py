import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(10, 5)
ax.set_title("Gráfico de Linhas")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], linestyle='-', color='b', label='Linha 1')
ax.legend()

plt.show()