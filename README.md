# Data Structures & Algorithms

## Start Here

🧱 [**Data Structures**](./ds.md)

🗺️ [**Algorithms**](./algo.md)

🤸🏽‍♂️ [**Dynamic Programming**](./dynamic.md)

<hr>

## Time Complexity

Good software engineering is about choosing data structures and algorithms that meet the functional requirements whilst optimising for time/space costs

| Complexity        | Big O Notation    | Example Operations                                |    
|:-----------------:|:-------------:    |:-----------------------------------------:        |
|Constant           |O(1)               |Assignment, index lookup, pop, push, print         | 
|Double Log         |O(log(log N))      |At each step, problem space is reduced by root(N)(i.e. N/root(N))<br/>ex.Interpolation Search|
|Log                |O(log N)           |At each step, problem space reduced by constant factor (i.e. N/c)<br/>ex.Binary Search, Bisection Search, Fibonacci Generator         |
|Linear             |O(N)               |Proportional to problem space<br/>ex. linear search, loops         |
|Log Linear         |O(N * log N)       |Log process at each iteration<br/>ex. Merge Sort, Heap Sort, Quick Sort|
|Polynomial         |O(N**c)            |Nested operations<br/>ex. Bubble Sort, Insertion Sort, Selection Sort, Nested loops of 'c' depth|
|Exponential        |O(c**N)            |Branched operations<br/>ex. Recursive calls|
|Factorial          |O(N!)              |Permutations<br/>ex. List permutations, brute graph traversal|

[Calculating Time Complexity](https://adrianmejia.com/how-to-find-time-complexity-of-an-algorithm-code-big-o-notation/)

<hr>

## Code Index

| TOPIC                               | 🐍 Python Code                                      | ➕ C++ Code |
|:-----------------------------------:|:-------------:                                      |:-------------:|
| [Arrays](./arrays.md)           | [Dynamic Array](./py/dynamic_array.py)<br/>[Selection Sort](./py/selection_sort.py)<br/>[Bubble Sort](./py/bubble_sort.py)<br/>[Insertion Sort](./py/insertion_sort.py)<br/>[Merge Sort](./py/merge_sort.py)<br/>[Quick Sort](./py/quick_sort.py)<br/>[Counting Sort](./py/counting_sort.py)<br/>[Radix Sort](./py/radix_sort.py)<br/>[Binary Search](./py/binary_search.py)                | [Dynamic Array](./cpp/array.cpp) |
| [Linked Lists](./linked_lists.md)| [Doubly linked list](./py/doubly_linked.py)     |  [Singly Linked List](./cpp/llist) |
| [Stacks & Queues](./stacks_queues.md)| [Stack](./py/stack.py)<br/>[Queue](./py/queue.py)    | [Stack](./cpp/stack.cpp)<br/>[Queue](./cpp/queue.cpp) |
| [Trees](./trees.md)| [Binary Search Tree](./py/bst.py)<br/>[AVL Tree](./py/avl.py) | [Binary Search Tree](./cpp/bst) |
| [Hash Tables](./hash_tables.md) | [Direct Access Array](./py/direct_access.py)<br/>[Hash Table](./py/hash_table.py)|
| [Priority Queues & Heaps](./heaps.md)| [Array PQ](./py/priority_q.py)<br/>[Max Heap](./py/max_heap.py)<br/>[Min Heap](./py/min_heap.py)<br/>[Min HeapDict](./py/min_heapdict.py) | 
| [Graphs](./graphs.md)|[Graph dsa](./py/graph.py)<br/>[DAG Relaxation](./py/dag.py)<br/>[Bellman-Ford](./py/bellman_ford.py)<br/>[Dijkstra](./py/dijkstra.py)<br/>[APSP & Johnson](./py/apsp.py) | [Graph](./cpp/graph) |
| [Dynamic Programming](./dynamic.md)|[Fibonacci, 0/1 Knapsack, LCS](./py/dp.py)<br/> |