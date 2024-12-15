from typing import Any

class Node:
    def __init__(self, valor: Any):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class DequeDinamico:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def Deque_e_vazia(self) -> bool:
        return self.tamanho == 0
    
    def Insere_inicio_deque(self, valor: Any):
        novo_no = Node(valor)
        if self.Deque_e_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no
        self.tamanho += 1

    def Insere_final_deque(self, valor: Any):
        novo_no = Node(valor)
        if self.Deque_e_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        self.tamanho += 1

    def Remove_inicio_deque(self) -> Any:
        if self.Deque_e_vazia():
            raise IndexError('Deque vazio!')
        valor = self.inicio.valor
        if self.tamanho == 1:
            self.inicio = None
            self.fim.anterior = None
        self.tamanho -=1
        return valor
    
    def Remove_final_deque(self) -> Any:
        if self.Deque_e_vazia():
            raise IndexError('Deque vazio!')
        valor = self.fim.valor
        if self.tamanho == 1:
            self.inicio = None
            self.fim = None
        else: 
            self.fim = self.fim.anterior
            self.fim.proximo = None
        self.tamanho -= 1
        return valor
    
    def imprimir(self):
        if self.Deque_e_vazia():
            print('Deque vazio!')
            return
        atual = self.inicio
        while atual:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print()