# Stacks & Queues

* Stacks and queues are limitied access data types (ADT/Interface)
* Implementations in Python:
    * Using the inbuilt `list` (dynamic array)
    * Importing `collections.deque` module (double ended queue)
* Stacks and Queues can also be implemented using static arrays -- requires handling fixed memory allocation
* C++ has `stack` and `queue` containers as part of its STL. Both use a `deque` container by default. 

## Stacks [🐍[Python](./py/stack.py)] [➕[C++](./cpp/stack.cpp)]
* Stacks follow the LIFO (last in, first out) principle -- imagine a stack of pancakes, the pancake you cook last gets put on the top of the stack, and is the first one you eat.
* Operations:
    * stack.push() -- add to top/front of the stack
    * stack.pop() -- remove from top/front of the stack
    * get_top -- retrieve value of top element
    * is_empty?
* All operations are O(1)

## Queues [🐍[Python](./py/queue.py)] [➕[C++](./cpp/queue.cpp)]
* Queues follow the FIFO (first in, first out) principle -- imagine a queue at the grocery store, the first person in line is the first person who gets served.
* Operations:
    * queue.enqueue() -- add element to the end of the queue
    * queue.dequeue() -- remove from front of the queue
    * get_front -- retrieve value of front element
    * is_empty?
* All operations are O(1) if `tail` is included on singly linked list

<hr>

### Resources:
* [Real Python - Implementing Stacks](https://realpython.com/how-to-implement-python-stack/#using-collectionsdeque-to-create-a-python-stack)
* [MIT 6006 Lesson 2](./notes/MIT6006/02%20Sequences%20and%20Sets.pdf)
* [UCSD Data Structures Fundamentals](https://www.edx.org/course/data-structures-fundamentals)