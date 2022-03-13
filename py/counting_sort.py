# RUN: python py/counting_sort.py

"""
Counting Sort algorithm
* Not inplace
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

def counting_sort(arr):
    # Determine key range for DAA
    u = max([x.key for x in arr]) # O(n)
    # Build DAA with arrays as chains (to implements queues)
    daa = [[] for _ in range(u+1)] # O(u)
    for x in arr:
        daa[x.key].append(x)
    # Replace values in input array
    idx = 0
    for chain in daa:
        for x in chain:
            arr[idx] = x
            idx += 1  

    return arr      

def main():
    array = random_data(10,20)
    print("UNSORTED")
    for a in array:
        print(a.key, a.val)
    print("********")
    print("SORTED")
    counting_sort(array)
    for a in array:
        print(a.key, a.val)

if __name__ == "__main__":
    main()

"""
UNSORTED
4 Christine Ryan
6 Adrian Sutton
17 Paige Kelly
5 Brian Reese
8 Tammy Davis
16 Steven Miller
2 Christopher Wilson
13 Willie Black
0 Samantha Haynes
20 Lisa Wilkerson
********
SORTED
0 Samantha Haynes
2 Christopher Wilson
4 Christine Ryan
5 Brian Reese
6 Adrian Sutton
8 Tammy Davis
13 Willie Black
16 Steven Miller
17 Paige Kelly
20 Lisa Wilkerson
"""