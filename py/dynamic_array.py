# RUN: python dsa/py/dynamic_array.py

"""
Dynamic Array

DynamicArray Interface Methods
* insert_end
"""
import numpy as np

class DynamicArray:
    def __init__(self, size):
        self.size = size
        self.length = 0
        self.arr = self.alloc_arr(size)
        self.resize_factor = 2

    def __len__(self):
        return self.length

    def __str__(self):
        return f'Array: {self.arr}, Length: {self.length}, Size: {self.size}'

    def alloc_arr(self,size):
        # Allocate an empty array of `size` elements
        return np.array([None]*size)
    
    def insert_end(self, val):
        # If array is at capacity
        if self.length == self.size:
            # Resize array by factor scaler
            self.resize_arr()
        # Insert val at end
        self.arr[self.length] = val
        # Total elements counter    
        self.length += 1

    def resize_arr(self):
        # Allocate new space
        new_size = self.resize_factor*self.size
        new_arr = np.array([None]*new_size)
        # Copy elements old -> new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        # Update self assignments
        self.arr = new_arr
        self.size = new_size


def main():
    darr = DynamicArray(5)
    print(darr)
    for i in range(2,11,2):
        darr.insert_end(i)
    print(darr)
    darr.insert_end(100)
    print(darr)

if __name__ == "__main__":
    main()

"""
OUTPUT:
Array: [None None None None None], Length: 0, Size: 5
Array: [2 4 6 8 10], Length: 5, Size: 5
Array: [2 4 6 8 10 100 None None None None], Length: 6, Size: 10
"""
