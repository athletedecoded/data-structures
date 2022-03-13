# RUN: python dsa/py/direct_access.py

"""
Direct Access Array built on Python list

DirectAccessArray Interface Methods:
* find
* insert
* delete
"""

class Data:
    def __init__(self, key, info):
        self.key = key
        self.info = info

class DirectAccessArray:
    def __init__(self, u):
        # allocate direct access array space
        self.arr = [None]*u
    
    def __str__(self):
        return f"{self.arr}"

    def find(self, k):
        return self.arr[k]
    
    def insert(self, x):
        self.arr[x.key] = x.info

    def delete(self, k):
        self.arr[k] = None

def main():
    x = Data(0, {"Name": "Harry Potter", "House": "Hogwarts"})
    y = Data(1, {"Name": "Hermione Granger", "House": "Hogwarts"})
    z = Data(3, {"Name": "Draco Malfoy", "House": "Slytherin"})

    inputs = [x,y,z]
    n = max([i.key for i in inputs])

    # Allocate direct access array size according to key values
    daa = DirectAccessArray(n+1)
    print(daa)

    for item in inputs:
        daa.insert(item)
    
    print(daa)

    print(f'Found {daa.find(x.key)} in O(1) time')


if __name__ == "__main__":
    main()

"""
OUTPUT
[None, None, None, None]
[{'Name': 'Harry Potter', 'House': 'Hogwarts'}, {'Name': 'Hermione Granger', 'House': 'Hogwarts'}, ...
... None, {'Name': 'Draco Malfoy', 'House': 'Slytherin'}]
Found {'Name': 'Harry Potter', 'House': 'Hogwarts'} in O(1) time
"""