# RUN: python dsa/py/selection_sort.py

"""
Selection Sort algorithm
* Iteratively selects and repositions the largest value in the array
* Inplace sort -- O(1) memory
* Not stable
"""

from random import randint

def random_array(n,max):
    return [randint(0,max) for _ in range(n)]

def selection_sort(arr):
    """
    Input: arr, list of integers
    Output: arr, inplace sorted array
    """
    sort_len = 0
    while sort_len < len(arr):
        # Init left most value as minimum
        min_idx = sort_len
        min_val = arr[sort_len]
        # Iterate over the portion of the array unsorted
        for idx, val in enumerate(arr[sort_len:]):
            if val < min_val:
                min_idx = idx + sort_len
                min_val = val
        # Swap left most value and minimum value
        arr[sort_len], arr[min_idx] = arr[min_idx], arr[sort_len]
        sort_len+= 1

    return arr

def main():
    array = random_array(20,30)
    print(array)
    sorted = selection_sort(array)
    print(sorted)

if __name__ == "__main__":
    main()

"""
OUTPUT
[7, 27, 8, 14, 5, 19, 29, 17, 8, 24, 8, 10, 6, 11, 11, 5, 13, 30, 3, 9]
[3, 5, 5, 6, 7, 8, 8, 8, 9, 10, 11, 11, 13, 14, 17, 19, 24, 27, 29, 30]
"""