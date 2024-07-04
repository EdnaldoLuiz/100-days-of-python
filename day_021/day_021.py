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

print("\nTamnho da deque é : ")

print(len(queue))

print("\nElemento no índice 2 é : ")

print(queue[2])