# RUN: python dsa/py/priority_q.py

"""
Priority Queue implementation

ArrayPQ Interface Methods:
* insert
* delete_max
* get_max
* sort
"""

from random import randint
from faker import Faker # conda install -c conda-forge faker
fake = Faker()

def random_data(n,max):
    # Randomly generates n data samples with x.key: random integer < max, x.val: random name
    return [Data(randint(0,max),fake.name()) for _ in range(n)]

class Data:
    def __init__(self, key, val):
        self.key = key
        self.val = val

# Base class of Priority Queue
class PriorityQ:
    def __init__(self):
        self.q = []

    def insert(self, x):
        self.q.append(x)

    def delete_max(self):
        # Assumes max key is in last array idx
        return self.q.pop()

    def get_max(self):
        # Assumes max key is in last array idx
        return self.q[-1]

# Array implementation of Priority Queue
class ArrayPQ(PriorityQ):
    def __init__(self):
        super().__init__()
    # Overwrite delete_max (need to put max element at end)
    def delete_max(self):
        n,q,max = len(self.q), self.q, 0
        for idx in range(1, n):
            if q[max].key < q[idx].key:
                max = idx
        # Swap max val to end
        q[max], q[idx] = q[idx], q[max]
        # Pop last elem
        return super().delete_max()
    
    def sort(self):
        """     
        * Sorts an array by loading it into a PQ
        * Pops all max elements: [max ➡ min]
        * Reverse array: [min ➡ max]
        """
        tmp = []
        while len(self.q) > 1:
            tmp.append(self.delete_max().key)
        # Add remaining element
        tmp.append(self.q[0].key)
        # Reverse tmp
        return [x for x in tmp[::-1]]

def main():
    data = random_data(10,40)
    pq = ArrayPQ()
    for d in data:
        pq.insert(d)
    print([x.key for x in pq.q])

    for _ in range(3):
        x = pq.delete_max()
        print(x.key, x.val)

    # test pq_sort
    print(pq.sort())



if __name__ == "__main__":
    main()

"""
OUTPUTS
[19, 29, 24, 14, 26, 39, 28, 3, 1, 3]
39 Karen Scott
29 Mandy Hammond
28 Clinton Ford
[1, 3, 3, 14, 19, 24, 26]
"""
        
