# RUN: python py/radix_sort.py

"""
Radix Sort algorithm
* Not inplace, stable 
"""

import math 
from counting_sort import counting_sort

class RadInt:
    def __init__(self, key, digits):
        self.key = key
        self.digits = digits
        self.val = key # init val as init key

def get_digits(x, c, b):
    """
    Split x into c digits of base powers
    """
    digits = []
    for _ in range(c):
        # Truncate last digit from x
        x, digit = divmod(x, b) # returns x // b, x % b
        digits.append(digit)
    
    return digits


def radix_sort(arr, base=10):
    """
    Inputs: 
        arr: list of integers
        base: integer base
    Output:
        arr: sorted array
    """
    u = max(arr) # O(n) find maximum key
    c = math.ceil(math.log(u,base)) # calc num digits
    n = len(arr)
    # tmp list to store key:digit pairs
    tmp = [None]*n
    for i in range(n):
        tmp[i] = RadInt(arr[i],get_digits(arr[i],c, base))
    # iterate over each digit
    for i in range(c): 
        # for each array item
        for j in range(n):
            # assign jth item key to == digit i
            tmp[j].key = tmp[j].digits[i]
            # call counting sort on tmp (recall will sort by tmp.key)
            counting_sort(tmp) 
    # Update arr[i] to value
    for i in range(n):
        arr[i] = tmp[i].val
    
    return arr


def main():
    A = [523,123,4,33,12]
    print(radix_sort(A))
    
    A = [1111,11,754,999,1010]
    print(radix_sort(A))

if __name__ == "__main__":
    main()

"""
OUTPUT
[4, 12, 33, 123, 523]
[11, 754, 999, 1010, 1111]
"""