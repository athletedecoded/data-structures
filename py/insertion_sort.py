# RUN: python dsa/py/insertion_sort.py

"""
Insertion Sort algorithm
* Inserts an element into the end position of an already sorted list
* Iteratively swaps element with item to its left, until it is in the correct position
* Inplace sort, stable
"""

from random import randint

def random_array(n,max):
    return [randint(0,max) for _ in range(n)]

def insertion_sort(arr):
    for idx in range(1, len(arr)): # O(n) loop over array from arr[1]:end
        j = idx # O(1) initialize arr[idx] as starting point -- arr[:idx] is sorted
        while j > 0 and arr[j] < arr[j - 1]: # O(i) loop over prefix
            arr[j - 1], arr[j] = arr[j], arr[j-1] # O(1) swap
            j = j - 1

    return arr

def main():
    array = random_array(20,30)
    print(array)
    sorted = insertion_sort(array)
    print(sorted)

if __name__ == "__main__":
    main()

"""
OUTPUT
[1, 1, 21, 21, 23, 27, 18, 9, 2, 3, 1, 30, 10, 16, 22, 17, 5, 18, 20, 21]
[1, 1, 1, 2, 3, 5, 9, 10, 16, 17, 18, 18, 20, 21, 21, 21, 22, 23, 27, 30]
"""