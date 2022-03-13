# RUN: python py/min_heapdict.py

"""
Min Heap Dictionary implementation from scratch
Heap dict has k:v pairs, where k are unique and v are priority values
Vs Min Heap where keys indicate priority order
Operations sort by priority value for use as a minimum priority queue

MinHeapDict Interface Methods:
* insert
* return_min
* get_min
* sort
"""

from random import randint

def random_data(n,min):
    data = []
    for i in range(n):
        data.append(Data(i, randint(0,min)))
    return data

class Data:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MinHeapDict:
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
        # if idx val < parent val, swap
        if self.q[i].val < self.q[p].val:
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
        # if left child within array and l.val < idx.val
        if ((l < self.n) and (self.q[l].val < self.q[c].val)):
            c = l
        # if right child within array and r.val < idx.val/l.ley
        if ((r < self.n) and (self.q[r].val < self.q[c].val)):
            c = r
        # if idx val is < child val, swap
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
            tmp.append(self.return_min().val)
        # Add remaining element
        tmp.append(self.q[0].val)
        # Reverse tmp
        return [x for x in tmp]


def main():
    data = random_data(10,20)
    h = MinHeapDict()
    h.insert(data)

    print([(x.key, x.val) for x in h.q])
    
    for _ in range(h.n + 1):
        try:
            d = h.return_min()
            print(f"Deleted ({d.key, d.val})")
        except:
            print("Nothing left in the heap")
    
    # Heap Sort
    print("Heap Sort")
    arr = random_data(10,20)
    sorted = h.sort(arr)
    print(f'{[a.val for a in arr]} --> {[x for x in sorted]}')

if __name__ == "__main__":
    main()

"""
OUTPUT
[(5, 0), (9, 0), (1, 2), (7, 11), (4, 5), (2, 19), (6, 8), (3, 18), (8, 13), (0, 14)]
Deleted ((5, 0))
Deleted ((9, 0))
Deleted ((1, 2))
Deleted ((4, 5))
Deleted ((6, 8))
Deleted ((7, 11))
Deleted ((8, 13))
Deleted ((0, 14))
Deleted ((3, 18))
Deleted ((2, 19))
Empty Queue, can't delete
Nothing left in the heap
Heap Sort
[8, 20, 1, 20, 13, 5, 14, 20, 8, 10] --> [1, 5, 8, 8, 10, 13, 14, 20, 20, 20]
"""