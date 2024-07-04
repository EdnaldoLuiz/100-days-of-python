# Desafio 21

Criando e manipulando um deque para operações de pilha e fila

## Explicação

### Ferramentas Utilizadas

- `collections.deque`: Estrutura de dados que suporta adições e remoções rápidas de ambos os lados.

### Funções Principais

- `deque.append()`: Adiciona um elemento ao final do deque.
- `deque.appendleft()`: Adiciona um elemento ao início do deque.
- `deque.popleft()`: Remove e retorna um elemento do início do deque.
- `deque.pop()`: Remove e retorna um elemento do final do deque.
- `len()`: Retorna o tamanho do deque.
- Indexação: Acessa elementos por índice.

## Resultado

```py
import collections
    
queue = collections.deque([1, 2, 3])
print(queue)

queue.append(4)
print("\nA deque depois de adicionar no final é : ")
print(queue)

queue.appendleft(6)
print("\nA deque depois de adicionar no início é : ")
print(queue)

print("\nA deque depois de remover do início é : ")
queue.popleft()
print(queue)

print("\nA deque depois de remover do final é : ")
queue.pop()
print(queue)

print("\nTamanho da deque é : ")
print(len(queue))

print("\nElemento no índice 2 é : ")
print(queue[2])