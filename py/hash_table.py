# RUN: python dsa/py/hash_table.py

"""
Hash Table
Implement buckets/chains using built in Python list (dynamic array)

HashTable Interface Methods:
* insert
* check_chains
* delete
* find
"""

from random import choice
from sympy import nextprime # conda install -c anaconda sympy
from faker import Faker # conda install -c conda-forge faker
fake = Faker()

def gen_universal_hash_fxn(a,b,p,n):
    """
    h(x) = (ax + b mod p) mod n
    where a, b ∈{0,...,p − 1} and a !=0
    """
    def hash_fxn(x):
        r = (a*x + b) % p
        return r % n
    return hash_fxn 

def random_hash(p,n):
    a = choice( range(1, p))
    b = choice(range(p))
    return gen_universal_hash_fxn(a,b,p,n)

class Data:
    """
    Data packet which has a key and associated value/information
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    def __init__(self, h, n):
        self.h = h
        self.table = [list() for _ in range(n)]
        self.len = 0
    
    def __len__(self):
        return self.len
    
    def check_chains(self):
        for i in range(len(self.table)):
            print(f'Chain {i} contains {len(self.table[i])} items')

    def insert(self,x):
        # Insert data object, x
        # Apply hash function to key -> insert value into chain at that table index
        self.table[self.h(x.key)].append(x.val)
        self.len += 1
    
    def delete(self, x):
        # Delete object x
        chain = self.table[self.h(x.key)]
        # Search for x in chain: O(n)
        for i in range(len(chain)):
            if chain[i] == x.val:
                self.len -= 1
                return chain.pop(i)
        return None

    def find(self, x):
        # Delete object x
        chain = self.table[self.h(x.key)]
        # Search for x in chain: O(n)
        for i in chain:
            if i == x.val:
                return i
        return None

def main():
    # Define number of data items
    M = 100
    # Define number of buckets
    n = 15

    # Find the next prime number after M
    p = nextprime(M)
    print(f'The next prime after {M} is {p}')

    # Generate M random people data with key = phone number, value = name
    people = []
    for i in range(M):
        people.append(Data(int(fake.msisdn()),fake.name()))

    print(f'Example data: {people[0].key, people[0].val}')

    # Create hash table using random universal hash function
    hash_table = HashTable(random_hash(p,n),n)

    for person in people:
        hash_table.insert(person)
    
    # Check chain allocations/collisions
    hash_table.check_chains()
    print(len(hash_table))

    # Find a person
    wally = hash_table.find(people[42])
    print(f'Found {wally}')

    # Delete a person
    p1 = hash_table.delete(people[77])
    print(f'Removed {p1}')
    print(len(hash_table))


if __name__ == "__main__":
    main()


"""
OUTPUT
The next prime after 100 is 101
Example data: (4294656001389, 'Erik Bond')
Chain 0 contains 8 items
Chain 1 contains 5 items
Chain 2 contains 8 items
Chain 3 contains 6 items
Chain 4 contains 5 items
Chain 5 contains 7 items
Chain 6 contains 12 items
Chain 7 contains 4 items
Chain 8 contains 3 items
Chain 9 contains 9 items
Chain 10 contains 9 items
Chain 11 contains 8 items
Chain 12 contains 8 items
Chain 13 contains 4 items
Chain 14 contains 4 items
100
Found Mackenzie Soto
Removed Michael Carter
99
"""
