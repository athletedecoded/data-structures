# RUN: python dsa/py/bubble_sort.py

"""
Bubble Sort Algorithm
* Pairwise comparison algorithm -- swaps adjacent elements until array is sorted
* Biggest element "bubbles" to the top
"""
from random import randint

def random_array(n,max):
    return [randint(0,max) for _ in range(n)]

def bubble_sort(arr):
    swaps = True
    while swaps:
        swaps = False
        # Over length of array
        for idx in range(len(arr)-1):
            # Compare side by side elements
            if arr[idx] > arr[idx+1]:
                # Swap if left elem > right elem
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                swaps = True
        
    return arr

def main():
    array = random_array(20,30)
    print(array)
    sorted = bubble_sort(array)
    print(sorted)

if __name__ == "__main__":
    main()
                
"""
OUTPUT
[13, 30, 8, 28, 19, 3, 10, 18, 13, 5, 30, 3, 15, 21, 24, 14, 16, 27, 20, 26]
[3, 3, 5, 8, 10, 13, 13, 14, 15, 16, 18, 19, 20, 21, 24, 26, 27, 28, 30, 30]
"""