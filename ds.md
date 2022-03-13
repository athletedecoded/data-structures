# Data Structures

* Specification: define the expected operations/behaviors.
* Interface: how the user calls/interacts with operations and methods. 
* Implementation: how the operations are performed.

The interface abstracts the implementations that meet the specification.

## Abstract Data Types (ADTs) vs Data Structures

**ADTs**

* ADT = an interface. In OOP, class implements the interface.
* For example, `stack` is an ADT. 
    * One *specification* of a stack is that it adheres to the LIFO principle (elements are added and removed from the top.
    * The *interface* for this behaviour are methods stack.append(), stack.pop().
    * A stack can be *implemented* in a number of ways -- the underlying data stucture could be a dynamic array or linked list, each having a trade-offs in operation complexity and the underlying code needed to achieve .pop and .append. 

**Data Structures**
* Data structures define how informtion is stored, retrieved and organised in system memory
* Each DS has an associated memory overhead, implementation, and optimises speed for different operations
* Choosing DS is about balancing complexity cost against the most frequent operations and information requirements 

<hr>

## Interfaces/ADTs

### Sequence/List
* Operations
    * build(X) 
    * len()
    * iter()
    * get(idx), set(idx)
    * insert(x, idx), delete(idx)
    * insert_start(x), delete_start()
    * insert_end(x), delete_end()
* Implementations
    * [Static Array](./arrays.md)
    * [Dynamic Array](./arrays.md)
    * [Linked List](./linked_lists.md)

### Stacks & Queues

➡ *Subset of the sequence/list interface (i.e. limited/specific operations)*
* [Stack](./queues_stacks.md) Operations
    * push(x) ➡ add to end/top 
    * pop() ➡ remove from end/top
* [Queue](./queues_stacks.md) Operations
    * enqueue(x) ➡ add to end 
    * dequeue() ➡ remove from start
* Implementations
    * [Dynamic Array](./arrays.md)
    * [Linked List](./linked_lists.md)
    * [Binary Tree/Balanced Binary Tree](./trees.md)

### Set
* Operations on x:{k,v} (data object x with key, val(s))
    * build(X) 
    * len()
    * find(k)
    * insert(x) ➡ insert obj x 
    * delete(k) ➡ delete by key
    * in_order() ➡ traverse in key order
    * find min(), find max() 
    * find next(k), find prev(k)
* Implementations
    * [Array](./arrays.md)
    * [Sorted Array](./algo.md)
    * [Direct Access Array](./hash_tables.md)
    * [Hash Table](./hash_tables.md)
    * [Binary Tree/Balanced Binary Tree](./trees.md)


### Priority Queue

➡ *Subset of the sequence/list interface (i.e. limited/specific operations)*
* Operations
    * build(X)
    * insert(x)
    * delete_max()
    * get_max()
* Implementations
    * [Array](./arrays.md)
    * [Sorted Array](./algo.md)
    * [Min/Max Binary Heap](./heaps.md)

### Map/Dictionary
* Set of {key:value} pairs, where keys must be unique
* Operations
    * build(X)
    * insert(k,v)
    * get(k), update(k)
    * delete(k)
* Implementations
    * [Hash Table](./hash_tables.md)
    * [Binary Search Tree](./trees.md)

### Graph
* Structure defined by a set of vertices and edges
* Edges can be weighted/unweighted and undirected/undirected
* Typically represented as an adjacency list, map or matrix
* Operations
    * insert(v), remove(v)
    * insert(e), remove(e)
    * get_neighbours(v)
    * shortest_path(v1, v2)
    * reachable(v1), path_exists(v1, v2)
* Implementations
    * [Graph](./graphs.md)

<hr>

## Complexity Comparison

![](./assets/BigO.png)