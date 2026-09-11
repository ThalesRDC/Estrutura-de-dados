from stack import Stack

class QueueUsingStacks:
    """
    IMPLEMENTAR O COMPORTAMENTO DE FILAS USANDO APENAS OPERAÇÕES DE PILHAS.
    Fila (Queue) implementada usando pilha (Stack)
    para manter o comportamento FIFO (First In, First Out).
    Implementar apenas enqueue, dequeue e is_empty abaixo.
    """
    def __init__(self):
        self.pilha_principal = Stack()   # Pilha onde inserimos os elementos.
        self.pilha_aux = Stack()         # Pilha auxiliar que deve ser usada.

    def enqueue(self, data):
        """
        Insere um elemento no final da fila.
        Empilha o novo elemento na pilha principal.
        """
        self.pilha_principal.push(data)

    def dequeue(self):
        """
        Remove e retorna o elemento do início da fila (FIFO).
        Se a pilha auxiliar estiver vazia, transfere todos os elementos
        da pilha principal para a auxiliar (invertendo a ordem).
        """
        if self.is_empty():
            raise IndexError("Fila vazia - Impossível remover elemento")

        if self.pilha_aux.is_empty():
            while not self.pilha_principal.is_empty():
                self.pilha_aux.push(self.pilha_principal.pop())

        return self.pilha_aux.pop()

    def is_empty(self):
        """
        Verifica se a fila está vazia.
        Retorna True se ambas as pilhas estiverem vazias, caso contrário False.
        """
        return self.pilha_principal.is_empty() and self.pilha_aux.is_empty()

    def peek(self):
        """
        Retorna o elemento do início da fila sem removê-lo (FIFO).
        Se a pilha auxiliar estiver vazia, transfere todos os elementos
        da pilha principal para a auxiliar (invertendo a ordem).
        """
        if self.is_empty():
            raise IndexError("Fila vazia - Impossível espiar elemento")

        if self.pilha_aux.is_empty():
            while not self.pilha_principal.is_empty():
                self.pilha_aux.push(self.pilha_principal.pop())

        return self.pilha_aux.peek()

    def size(self):
        """
        Retorna o total de elementos presentes na fila.
        """
        return self.pilha_principal.size() + self.pilha_aux.size()

    def __len__(self):
        return self.size()

    def __str__(self):
        temp_principal = Stack()
        temp_aux = Stack()
        result = []

        while not self.pilha_aux.is_empty():
            val = self.pilha_aux.pop()
            result.append(val)
            temp_aux.push(val)

        while not self.pilha_principal.is_empty():
            val = self.pilha_principal.pop()
            temp_principal.push(val)

        while not temp_principal.is_empty():
            val = temp_principal.pop()
            result.append(val)
            self.pilha_principal.push(val)

        while not temp_aux.is_empty():
            self.pilha_aux.push(temp_aux.pop())

        if not result:
            return "Fila vazia"

        if len(result) == 1:
            return f"{result[0]} (Início e Fim)"

        result[0] = f"{result[0]} (Início)"
        result[-1] = f"{result[-1]} (Fim)"
        return "\nv\n".join(str(x) for x in result)


# Testando a fila
if __name__ == "__main__":
    fila = QueueUsingStacks()

    print("\nInserindo: 10, 20, 30")
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    print(fila)
    print(f"Primeiro elemento (peek): {fila.peek()}")
    print(f"Tamanho da fila: {fila.size()}")

    print("\nRemovendo dois elementos:")
    print(fila.dequeue())
    print(fila.dequeue())
    fila.enqueue(40)

    print("\nEstado atual da fila:")
    print(fila)

    print("\nA fila está vazia?", fila.is_empty())

    print("\nRemovendo mais um elemento:")
    print(fila.dequeue())

    print("\nA fila está vazia?", fila.is_empty())

    print("\nEstado atual da fila (1 elemento):")
    print(fila)

    print("\nRemovendo o último elemento:")
    print(fila.dequeue())

    print("\nA fila está vazia?", fila.is_empty())
    print(fila)

    print("\nTentando remover de fila vazia:")
    try:
        fila.dequeue()
    except IndexError as e:
        print(f"Erro esperado: {e}")