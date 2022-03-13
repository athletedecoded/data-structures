# RUN: python dsa/py/doubly_linked.py

"""
Doubly linked list with HEAD and TAIL pointers

DList Interface Methods:
* is_empty
* insert_start
* pop_start
* insert_end
* pop_end
* insert_before
* traverse_fwd
* traverse_bwd
"""
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.head
        yield node
        while node.next is not None:
            node = node.next
            yield node

    def __reversed__(self):
        node = self.tail
        while node is not self.head:
            yield node
            node = node.prev
        yield self.head
    
    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False
    
    def insert_start(self, val):
        node = Node(val)
        # If the list is empty, assign node as head and tail
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            # point head to new node
            self.head = node
        # increment length counter
        self.length += 1
    
    def pop_start(self):
        if self.is_empty():
            raise Exception("Cannot remove from empty list")
        # repoint head
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        
        self.length -= 1
        return node.val

    def insert_end(self, val):
        node = Node(val)
        # If the list is empty, assign node as head and tail
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            # point tail to new node
            self.tail = node
        # increment length counter
        self.length += 1

    def pop_end(self):
        if self.is_empty():
            raise Exception("Cannot remove from empty list")
        # repoint tail
        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        
        self.length -= 1
        return node.val

    def insert_before(self, val, i):
        """
        Improve function efficiency by choosing the shortest traversal 
        direction from head (i <= self.length/2) or tail (i > self.length/2)
        """
        new_node = Node(val)
        # idx must be positive and within the length of the list
        if ((i < 0) or (i >= self.length)):
            raise Exception("Index must be > 0 and within the length of the list")
        # if inserting before 0th node
        if i == 0:
            self.insert_start(val)
            return
        # if index in left half, traverse forward from head until index
        if i <= self.length/2:
            print("Approaching from head")
            node = self.head
            # Traverse until ith positon
            for _ in range(i):
                node = node.next
                prev_node = node.prev
        else:
        # Traverse from tail backwards to index
            print("Approaching from tail")
            node = self.tail
            # Traverse until ith positon
            for _ in range(self.length - i):
                node = node.prev
                prev_node = node.prev
        
        # insert new node between ith node and prev_node ie. (i-1)th node
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = node
        node.prev = new_node

        self.length += 1           
    
    @staticmethod
    def traverse_fwd(dlist):
        print('HEAD', end=' -> ')
        if not dlist.is_empty():
            for node in dlist:
                print(node.val,end=' -> ')
        print('TAIL')

    @staticmethod
    def traverse_bwd(dlist):
        print('TAIL', end=' -> ')
        if not dlist.is_empty():
            for node in reversed(dlist):
                print(node.val,end=' -> ')
        print('HEAD')

def main():
    dlist = DList()
    dlist.insert_start(5)
    dlist.insert_start(14)
    dlist.insert_end(2)
    dlist.insert_end("cat")

    DList.traverse_fwd(dlist)
    print(f'length: {len(dlist)}')

    print(f'Popped start: {dlist.pop_start()}')
    print(f'Popped end: {dlist.pop_end()}')

    dlist.insert_end(8)
    dlist.insert_end("dog")

    dlist.insert_before(99,2)
    dlist.insert_before("pickle",0)
    dlist.insert_before(42,5)

    DList.traverse_fwd(dlist)
    DList.traverse_bwd(dlist)
    print(f'length: {len(dlist)}')


if __name__ == "__main__":
    main()

"""
OUTPUT:
HEAD -> 14 -> 5 -> 2 -> cat -> TAIL
length: 4
Popped start: 14
Popped end: cat
Approaching from head
Approaching from tail
HEAD -> pickle -> 5 -> 2 -> 99 -> 42 -> 8 -> dog -> TAIL
TAIL -> dog -> 8 -> 42 -> 99 -> 2 -> 5 -> pickle -> HEAD
length: 7
"""