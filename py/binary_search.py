# RUN: python dsa/py/binary_search.py

"""
Array Based Binary Search Algorithm
"""

def binary_search(arr, val, lo = None, hi = None):
    """
    Recursively search for val in sorted array
    Returns idx of val position, -1 if not in array
    """
    if lo is None:
        lo = 0 # low value idx
    if hi is None:
        hi = len(arr) - 1 # high value idx

    # base case
    if hi < lo:
        return -1

    # Find middle idx
    mid = (lo + hi) // 2

    # Check if val is at mid idx
    if arr[mid] == val:
        return mid
    # if val < arr[mid], search left half array
    if val < arr[mid]:
        return binary_search(arr,val, lo, mid -1)
    # if val > arr[mid], search right half
    if val > arr[mid]:
        return binary_search(arr,val, mid + 1, hi)


def main():
    array = [11,3,6,7,92,1,77,42]
    print(array)
    array.sort()
    print(array)

    print(f"Index of value: {binary_search(array, 1)}")
    print(f"Index of value: {binary_search(array, 12)}")
    print(f"Index of value: {binary_search(array, 77)}")

if __name__ == "__main__":
    main()
                
"""
OUTPUT
[11, 3, 6, 7, 92, 1, 77, 42]
[1, 3, 6, 7, 11, 42, 77, 92]
Index of value: 0
Index of value: -1 i.e. not found
Index of value: 6
"""

