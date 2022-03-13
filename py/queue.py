
# RUN: python dsa/py/queue.py

"""
Queue implementation
1) inbuilt python list
2) deque library
3) from scratch using singly linked list

Queue Interface Methods
* is_empty
* enqueue
* dequeue
* print_queue
"""

from collections import deque

# Queues as dynamic arrays using `list`
def array_queue():
    q = list()
    for i in range(10):
        q.append(i)
    print(f'Dequeued: {q.pop(0)}')
    print(q)

# queues using deque
def deque_queue():
    q = deque()
    for letter in ['a','b','c','d','e','f']:
        q.append(letter)
    print(f'Dequeued: {q.popleft()}')
    print(q)

# queues using singly linked lists with `tail`
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
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

    def enqueue(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Cannot remove from empty queue")
        else:
            node = self.head
            self.head = self.head.next
        
        self.length -= 1
        return node.val
    
    def get_first(self):
        return self.head.val

    @staticmethod
    def print_queue(queue):
        print('HEAD', end=' -> ')
        if not queue.is_empty():
            for node in queue:
                print(node.val,end=' -> ')
        print('TAIL')


def main():
    array_queue()
    deque_queue()

    q = Queue()
    Queue.print_queue(q)
    nums = [1,2,3,5,7]
    for n in nums:
        q.enqueue(n)
    Queue.print_queue(q)
    print(f'Dequeued: {q.dequeue()}')
    Queue.print_queue(q)
    print(q.get_first())
    print(f'length: {len(q)}')


if __name__ == "__main__":
    main()

"""
OUTPUT:
Dequeued: 0
[1, 2, 3, 4, 5, 6, 7, 8, 9]
Dequeued: a
deque(['b', 'c', 'd', 'e', 'f'])
HEAD -> TAIL
HEAD -> 1 -> 2 -> 3 -> 5 -> 7 -> TAIL
Dequeued: 1
HEAD -> 2 -> 3 -> 5 -> 7 -> TAIL
2
length: 4
"""
