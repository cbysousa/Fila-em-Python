from typing import Deque, Any
from collections import deque

fila: Deque[Any] = deque()

#Adicionando elementos à fila (enqueue)
fila.append('A')
fila.append('B')
fila.append('C')

print("Fila:", fila) # Exibe a fila antes das remoções

#Removendo elementos da fila (dequeue) com tratamento de erro
while fila:  #Continua enquanto a fila não estiver vazia
    try:
        removido = fila.popleft()
        print('Removido:', removido)
    except IndexError:  #Captura o erro se a fila estiver vazia
        print("A fila está vazia.")
        break  #Sai do loop

print("Fila:", fila) #Exibe a fila vazia
