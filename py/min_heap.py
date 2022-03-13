# RUN: python dsa/py/min_heap.py

"""
Min Heap and Heap Sort implementation from scratch
* Not stable, in-place

MinHeap Interface Methods
* insert
* return_min
* get_min
* sort 
"""

from random import randint
from faker import Faker # conda install -c conda-forge faker
fake = Faker()

def random_data(n,min):
    # Randomly generates n data samples with x.key: random integer < min, x.val: random name
    return [Data(randint(0,min),fake.name()) for _ in range(n)]

class Data:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MinHeap:
    def __init__(self):
        self.q = []
        self.n = 0

    def insert(self, arr): # O(log n)
        for x in arr:
            self.q.append(x)
            self.n += 1
            self.minify_up(self.n - 1)
    
    def return_min(self): # O(log n) 
        if self.n == 0:
            print("Empty Queue, can't delete")
            return
        # swap root and right-most leaf nodes
        self.q[0], self.q[self.n-1] = self.q[self.n-1], self.q[0]
        rv = self.q.pop()
        self.n -= 1
        self. minify_down(0) # push root node down

        return rv
    
    def get_min(self):
        return self.q[-1]

    # Min Heapify Up, for node at q[i]
    def minify_up(self, i):
        """
        Propogates smallest nodes up
        """
        # if i is root node, stop
        if i < 1:
            return
        # Get parent
        p = self.parent(i)
        # if idx key < parent key, swap
        if self.q[i].key < self.q[p].key:
            self.q[i], self.q[p] = self.q[p], self.q[i]
            # Recurse on parent node
            self.minify_up(p)
    
    # Min Heapify Down
    def minify_down(self, i):
        """
        Propogates largest nodes down
        """
        l, r = self.left(i), self.right(i)
        c = i
        # if left child within array and l.key < idx.key
        if ((l < self.n) and (self.q[l].key < self.q[c].key)):
            c = l
        # if right child within array and r.key < idx.key/l.ley
        if ((r < self.n) and (self.q[r].key < self.q[c].key)):
            c = r
        # if idx key is < child key, swap
        if c != i:
            # print("Swapping",self.q[i].key, self.q[c].key)
            self.q[i], self.q[c] = self.q[c], self.q[i]
            # Recurse on child
            self.minify_down(c)

    def parent(self, i):
        return (i -1) // 2
    
    def left(self, i):
        # Check child idx within array space
        return 2*i + 1

    def right(self, i):
        return 2*i + 2
    
    def sort(self, arr):
        self.insert(arr)
        tmp = []
        while len(self.q) > 1:
            tmp.append(self.return_min().key)
        # Add remaining element
        tmp.append(self.q[0].key)
        # Reverse tmp
        return [x for x in tmp]


def main():
    data = random_data(10,20)
    h = MinHeap()
    h.insert(data)

    print([x.key for x in h.q])
    
    for _ in range(h.n + 1):
        try:
            print(f"Deleted {h.return_min().key}")
        except:
            print("Nothing left in the heap")
    
    # Heap Sort
    print("Heap Sort")
    arr = random_data(10,20)
    sorted = h.sort(arr)
    print(f'{[a.key for a in arr]} --> {[x for x in sorted]}')

if __name__ == "__main__":
    main()

"""
OUTPUT
[17, 17, 16, 15, 12, 4, 13, 6, 7, 4]
Deleted 17
Deleted 17
Deleted 16
Deleted 15
Deleted 13
Deleted 12
Deleted 7
Deleted 6
Deleted 4
Deleted 4
Empty Queue, can't delete
Nothing left in the heap
Heap Sort
[18, 14, 13, 12, 11, 17, 1, 17, 15, 3] --> [1, 3, 11, 12, 13, 14, 15, 17, 17, 18]
"""


