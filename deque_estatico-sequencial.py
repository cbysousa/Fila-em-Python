from typing import Any

class DequeEstatico:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.deque = [None] * capacidade #Inicicaliza com None
        self.inicio = -1
        self.fim = -1
        self.tamanho = 0

    def Inicializar_Deque(self):
        self.inicio = -1
        self.fim = -1
        self.tamanho = 0

    def Deque_e_vazia(self) -> bool:
        return self.tamanho == 0
    
    def Deque_e_cheia(self) -> bool:
        return self.tamanho == self.capacidade
    
    def Insere_inicio_deque(self, valor:Any):
        if self.Deque_e_cheia():
            raise OverflowError('Deque cheio!')
        if self.Deque_e_vazia():
            self.inicio = self.fim = 0
        elif self.inicio == 0:
            self.inicio = self.capacidade -1
        else:
            self.inicio -= 1
        self.deque[self.inicio] = valor
        self.tamanho += 1

    def Insere_final_deque(self, valor:Any):
        if self.Deque_e_cheia():
            raise OverflowError('Deque cheio!')
        if self.Deque_e_vazia():
            self.inicio = self.fim = 0
        elif self.fim == self.capacidade -1:
            self.fim = 0
        else:
            self.fim += 1

        self.deque[self.fim] = valor
        self.tamanho += 1

    def Remove_inicio_deque(self) -> Any:
        if self.Deque_e_vazia():
            raise IndexError('Deque vazio!')
        
        valor = self.deque[self.inicio]
        self.deque[self.inicio] = None

        if self.inicio == self.fim:
            self.Inicializar_Deque
        elif self.inicio == self.capacidade-1:
            self.inicio = 0
        else:
            self.inicio += 1
        
        self.tamanho -= 1
        return valor
    
    def Remove_final_deque(self) -> Any:
        if self.Deque_e_vazia():
            raise IndexError('Deque vazio!')
        
        valor = self.deque[self.fim]
        self.deque[self.fim] = None

        if self.inicio == self.fim:
            self.Inicializar_Deque()
        elif self.fim == 0:
            self.fim = self.capacidade -1
        else:
            self.fim -= 1

        self.tamanho -= 1
        return valor
    
    def imprimir(self):
        if self.Deque_e_vazia():
            print('Deque vazio!')
            return
        
        for i in range(self.tamanho):
            indice = (self.inicio + i) % self.capacidade
            print(self.deque[indice], end=" ")
        print()

if __name__ == '__main__':
    # Exemplo de uso:
    deque = DequeEstatico(5)
    deque.Insere_inicio_deque(10)
    deque.Insere_final_deque(20)
    deque.Insere_inicio_deque(5)
    deque.imprimir()  # Output: 5 10 20
    deque.Remove_inicio_deque()
    deque.imprimir()  # Output: 10 20
    deque.Insere_final_deque(30)
    deque.Insere_inicio_deque(2)
    deque.Insere_final_deque(40)


    deque.imprimir() # Output 2 10 20 30 40
    deque.Remove_final_deque()
    deque.imprimir() # Output 2 10 20 30

    deque.Insere_final_deque(50)

    deque.imprimir() # Output 2 10 20 30 50

    deque.Remove_inicio_deque()
    deque.Remove_inicio_deque()
    deque.Remove_inicio_deque()
    deque.Remove_inicio_deque()
    deque.Remove_inicio_deque()
    deque.imprimir() #Deque vazio


    deque.Insere_final_deque(1) # adiciona normalmente depois de reinicializar
    deque.imprimir() # 1