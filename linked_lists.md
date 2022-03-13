# Linked Lists

* Built from a series of nodes where each node stores a value and a pointer to the next node
* `HEAD` is a pointer to the first node in the list
* `TAIL` is an pointer to the last node in the list
* Don't need to be declared with an inital size, unlike arrays

## Singly Linked Lists [➕[C++](./cpp/llist)]
* The node pointer is directed to the `NEXT` successive node
* Traversal is unidirectional from the start ➡ end of the list
* End of the list is indicated by the `TAIL` or when node.next == None


## Doubly Linked Lists [🐍[Python](./py/doubly_linked.py)]
* Two node pointers:
    1. `NEXT` is pointed to the successive node
    2. `PREV` is pointed at the previous/preceeding node
* Traversal is bidirectional along start ↔ end of the list
* End of the list is indicated by the `TAIL` or when node.next == None
* Start of the list is indicated by the `HEAD` or when node.prev == None

|Operation              | Singly Linked    | Doubly Linked | Notes |
|----------             |:----:            |:----:         |:-----:|
|get/set start          | O(1)             | O(1)          |       |
|insert start           | O(1)             | O(1)          |       |
|delete start           | O(1)             | O(1)          |       |      
|get/set end            | O(N)             | O(N)          | If `TAIL` then O(1)        |
|insert end             | O(N)             | O(N)          | If `TAIL` then O(1)        |
|delete end             | O(N)             | O(1)          |       |
|get/set ith node       | O(N)             | O(N)          |       |
|insert before ith node | O(N)             | O(1)          |       |
|insert after ith node  | O(1)             | O(1)          |       |
|delete i               | O(N)             | O(N)          |       |

<hr>

## Arrays vs Linked Lists

* Arrays require contiguos memory allocation to represent element order.
* Linked lists use pointers to store element order in memory. This allows for dynamic resizing but the tradeoff is more memory overhead to store 2 pointers (next, prev) for every node.
* Arrays are random access data structures. Linked lists are sequential access data structures (ie. sequential steps are needed to access values).
* Static arrays are best for index-based access and operations ~ O(1).
* Dynamic arrays are best for appending/popping last elements in a list ~ O(1).
* Linked lists are best for appending/popping first elements in a list and inserting into the middle of the list ~ O(1).
* Doubly linked lists improve efficiency of `pop end` and `insert before` operations ~ O(1). 


<hr>

### Resources:
* [UCSD Data Structures Fundamentals](https://www.edx.org/course/data-structures-fundamentals)
* [MIT 6006 Lesson 2](./notes/MIT6006/02%20Sequences%20and%20Sets.pdf)