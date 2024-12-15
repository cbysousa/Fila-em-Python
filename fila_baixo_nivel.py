from typing import Any, Iterator

EMPTY_NODE_VALUE = '__EMPTY_NODE_VALUE__'

class EmptyQueueError(Exception):
    ...

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Node

    def __repr__(self) -> str:
        return f'{self.value}'
    
    def __bool__(self) -> bool:
        return bool(self.value!= EMPTY_NODE_VALUE)
    
class Fila:
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = Node(EMPTY_NODE_VALUE)
        self._count = 0
    
    def enqueue(self, node_value: Any) -> Node:
        new_node = Node(node_value)

        if not self.first:
            self.first = new_node

        if not self.last:
            self.last = new_node
        
        else:
            self.last.next = new_node
            self.last = new_node
        
        self._count += 1

    def dequeue(self) -> Node:
        if not self.first:
            raise EmptyQueueError('Fila Vazia!')
        
        first = self.first

        if hasattr(self.first, 'next'):
            self.first = self.first.next
        
        else:
            self.first = Node(EMPTY_NODE_VALUE)

        self._count -= 1
        return first
    
    def peek(self) -> Node:
        return self.first
    
    def __len__(self) -> int:
        return self._count
    
    def __bool__(self) -> bool:
        return bool(self._count)
    
    def __iter__(self) -> Iterator[Any]: # Use Iterator[Any] as the return type
        self._iter_node = self.first # Initialize an iterator node
        return self
    
    def __next__(self) -> Any:
        if not self._iter_node:  # Check if the iterator node is empty
            raise StopIteration
        
        next_value = self._iter_node.value
        self._iter_node = self._iter_node.next if hasattr(self._iter_node, 'next') else None # Move to the next node
        return next_value # Return the value
        
    def __repr__(self) -> str:
        nodes = []
        current = self.first
        while current:
            nodes.append(repr(current.value))
            current = current.next if hasattr(current, 'next') else None
        return f'Queue({", ".join(nodes)})'
        
if __name__ == '__main__':
    fila = Fila()
for item in ['A', 'B', 'C']:
    fila.enqueue(item)
    print(fila)

for _ in range(3):  # Desenfileirar 3 vezes
    fila.dequeue()
    print(fila)