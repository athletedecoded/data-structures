# RUN: python py/merge_sort.py

"""
Merge Sort algorithm
* Recursively sort the left and right half of the array, then merge the two halves
* Not inplace - O(n) tmp memory space
* Stable
"""
from random import randint

def random_array(n,max):
    return [randint(0,max) for _ in range(n)]

def merge_sort(arr):
    """
    Function to recursively split and merge an array
    into L/R halves until sorted
    """
    # Base case: array of 1 element
    if len(arr) <= 1:
        return arr
    
    # Find mid point
    c = len(arr) // 2
    # Recursively split and sort left half of array
    L = merge_sort(arr[:c])
    # Recursively split and sort right half of array
    R = merge_sort(arr[c:])

    # Merge left and right side
    return merge(L,R)

def merge(L,R):
    """
    Function which joins L and R arrays into sorted array
    Inputs:
        L, R: arrays, left and right halves of array, respectively
    Output:
        tmp: array, sorted and merged array
    """
    tmp = []
    i,j = 0,0
    # While still unsorted elements in either half
    while (i < len(L) and j < len(R)):
        if L[i] < R[j]:
            tmp.append(L[i])
            i += 1
        else:
            tmp.append(R[j])
            j += 1
    # If either side has remaining items, we can assume 
    # they are in sorted order and add to end of tmp
    if i != len(L):
        tmp.extend(L[i:])
    if j != len(R):
        tmp.extend(R[j:])
    
    return tmp


def main():
    array = random_array(20,30)
    print(array)
    sorted = merge_sort(array)
    print(sorted)

if __name__ == "__main__":
    main()

"""
OUTPUT
[9, 9, 6, 23, 28, 19, 14, 22, 20, 3, 14, 5, 22, 6, 24, 3, 2, 24, 20, 0]
[0, 2, 3, 3, 5, 6, 6, 9, 9, 14, 14, 19, 20, 20, 22, 22, 23, 24, 24, 28]
"""