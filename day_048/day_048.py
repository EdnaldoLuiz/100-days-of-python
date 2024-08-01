import random

numero = random.random()
print(numero)

numero = random.randint(0, 100)
print(numero)

numero = random.randrange(0, 100, 5)
print(numero)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(lista)
print(lista)

elemento = random.choice(lista)
print(elemento)