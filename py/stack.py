# RUN: python py/stack.py

"""
Stack implementations
1) inbuilt python list
2) deque library
3) from scratch using singly linked list

Stack Interface Methods
* is_empty
* push
* pop
* get_top
* print_stack
"""
from collections import deque

# Stacks as dynamic arrays using `list`
def array_stack():
    stack = list()
    for i in range(10):
        stack.append(i)
    print(f'Popped: {stack.pop()}')
    print(stack)

# Stacks using deque
def deque_stack():
    stack = deque()
    for letter in ['a','b','c','d','e','f']:
        stack.append(letter)
    print(f'Popped: {stack.pop()}')
    print(stack)

# Stacks using singly linked lists
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.length = 0
        self.head = None
    
    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.head
        yield node
        while node.next is not None:
            node = node.next
            yield node
    
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot remove from empty stack")
        else:
            node = self.head
            self.head = self.head.next
        
        self.length -= 1
        return node.val

    def get_top(self):
        return self.head.val

    @staticmethod
    def print_stack(stack):
        print('HEAD', end=' -> ')
        if not stack.is_empty():
            for node in stack:
                print(node.val,end=' -> ')
        print('None')


def main():
    array_stack()
    deque_stack()

    stack = Stack()
    Stack.print_stack(stack)
    stack.push(4)
    stack.push(8)
    stack.push(12)
    Stack.print_stack(stack)
    print(f'Popped: {stack.pop()}')
    Stack.print_stack(stack)
    print(stack.get_top())
    print(len(stack))


if __name__ == "__main__":
    main()


"""
OUTPUT:
Popped: 9
[0, 1, 2, 3, 4, 5, 6, 7, 8]
Popped: f
deque(['a', 'b', 'c', 'd', 'e'])
HEAD -> None
HEAD -> 12 -> 8 -> 4 -> None
Popped: 12
HEAD -> 8 -> 4 -> None
8
2
"""
