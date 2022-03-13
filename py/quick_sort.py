# RUN: python dsa/py/quick_sort.py

"""
Quick Sort Algorithm
* Select a pivot and recursively partition array into values <, >, = to pivot
* Recursively call function on smaller arrays until base case (1 item)
* Not inplace (?), not stable
"""
from random import randint, choice

def random_array(n,max):
    return [randint(0,max) for _ in range(n)]

def quick_sort(arr):
    """
    Quicksort implementation using Python lists
    """
    # Base case: array of 1 element
    if len(arr) <= 1:
        return arr
    # Allocate tmp arrays
    less, equal, greater = [], [], []
    # Generate random pivot
    pivot = choice(arr)

    for a in arr:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            greater.append(a)
        else:
            equal.append(a)
      
    return quick_sort(less) + equal + quick_sort(greater)


def main():
    array = random_array(20,30)
    print(array)
    sorted = quick_sort(array)
    print(sorted)

if __name__ == "__main__":
    main()

"""
OUTPUT
[28, 15, 13, 2, 1, 21, 14, 27, 5, 4, 20, 13, 28, 22, 12, 4, 5, 12, 27, 29]
[1, 2, 4, 4, 5, 5, 12, 12, 13, 13, 14, 15, 20, 21, 22, 27, 27, 28, 28, 29]
"""