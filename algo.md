# Algorithms

## Search Algorithms

* Unsorted data ➡ linear search ~ O(n)
* Sorted data ➡ binary search ~ O(log n)
* For data structures there is a tradeoff between the cost of search vs cost of sort

|Data Structure |Build          |Find k    | Find min/max | Find prev/next |
|----------     |:-------:      |:--------:|:--------:    |:-------:       |
|Array          |O(N)           |O(N)      | O(N)         |  O(N)          |
|Sorted Array   |O(N * log N)   |O(log N)  | O(1)         |  O(log N)      |

To use binary search, we need to have a sorted DS -- so how should we sort it?

<hr>

## Sorting Algorithms
Input: array/list of n keys ➡ Output: sorted array/list

Terminology:
* "Destructive" = overwrites input array
* "In place" = Uses O(1) extra space ➡ constant memory
* "Stable" = Keys of the same value will remain in the same order when sorted

**Approaches/paradigms**
* Brute Force
    * Implemented iteratively/linearly -- where each item is checked against all other items.
* Divide & Conquer
    * Recursively divide and solve the search/sort space until the base case is reached (typically when size == 1).
    * The results are then combined into a final answer.
* [Dynamic Programming](./dynamic.md)
    * Recursion + memoization
    * Reduces problem space to constant-sized subproblems

### **Comparison Based Sort (Lower Bound n*log(n))**

* **Permutation/Bogo Sort**
    * Enumerate all permutations of array, check which one is in order
    * Permute cost: W(N!)
    * Check if permutation is sorted: W(N)
    * Total cost: W(N! * N) -- W is the lower bound cost 

* **[Selection Sort](./py/selection_sort.py)**
    * Iteratively selects and repositions the largest value in the array

* **[Insertion Sort](./py/insertion_sort.py)**
    * Iteratively swaps element with item to its left, until it is in the correct position

* **[Bubble Sort](./py/bubble_sort.py)**
    * Pairwise comparison algorithm -- swaps adjacent elements until array is sorted

* **[Merge Sort](./py/merge_sort.py)**
    * Recursively sort the left and right half of the array, then merge the two halves

* **[Quick Sort](./py/quick_sort.py)**
    * Select a pivot and recursively partition array into values <, >, = to pivot 

* **TimSort**
    * Hybrid of insertion sort and merge sort
    * Divides array into smaller 'runs`. Runs are sorted using insertion sort then merged.
    * Python's sorted() and sort() methods use TimSort
    * Stable

* **[Priority Queue Sort](./py/priority_q.py)**
    * Sorts an array by loading it into a PQ ➡ Pop all max elements ➡ Reverse order

* **[Heap Sort](./py/max_heap.py)**
    * PQ sort using a heap to provide logarithmic performance

### **Non Comparison Sorting**

A large value 'k' can be represented by two smaller values (a,b)
a = k//n, b = k % n, k = a*n +b
In python: a,b = divmod(k,n)
We could sort n unique keys by placing them in a direct access array, and iterating over the array
Limitations: large memory allocation, cannot have repeated keys

* **[Counting Sort](./py/counting_sort.py)**
    * Create an array A of r chains where each chain is a queue interface (dynamic array/linked list)
    * For each element x, add to the end of the queue A[x.key]
    * Concatenate all the chains: A[0], . . . ,A[r − 1]
    * Queue interface allows for stable algorithm
    * Assumes positive, integer keys
    * Not inplace
    * Runs in O(n + u) time. When u = O(n), then complexity is O(n)

* **[Radix Sort](./py/radix_sort.py)**
    * Extension of counting sort + tuple sort to represent larger key range
    * For x.key in base n, divide x.key into tuples of length c = logn(u) digits
    * Recursively call counting sort on n^0 th digit to n^(c-1)th digit
    * Example: if 5824 is the largest item in an array of base 10 keys 
        * Num digits, c: log10(5824) ~ 4
        * Construct tuple of powers of n: (10^3, 10^2, 10^1, 10^0) = (5,8,2,4)
    * Not inplace, stable

<hr>

## Graph-Algorithms

* **Breadth-First Search (BFS)  [🐍[Python](./py/graph.py)] [➕[C++](./cpp/graph)]**
    * Level-order graph search
    * Used to determine unweighted shortest path between two nodes

* **Depth-First Search (DFS) [🐍[Python](./py/graph.py)] [➕[C++](./cpp/graph)]**
    * Recursive hierarchical order graph search
    * Used to determine reachability/connectedness

* **[Topo Sort](./py/graph.py)**
    * Topographical ordering of a Directed Acyclic Graph(DAG) using DFS

* **[DAG Relaxation](./py/dag.py)**
    * Iteratively "relax" edge weights until optimal shortest path
    * Uses triangle inequality to determine UB for convergence

* **[Bellman-Ford](./py/bellman_ford.py)**
    * Relax every edge in the graph |V|−1 times 
    * At termination, if any edge is still relaxable ➡ graph contains negative weight cycle

* **[Dijkstra's](./py/dijkstra.py)**
    * Use minimum priority queue to relax node with minumum distance estimate
    * O(|V|*log|V|+|E|) for Fibonacci Heap PQ

* **[Johnson's](./py/apsp.py)**
    * All-Pairs Shortest Path for negative weight graph
    * Reweights graph edges and solves V * Dijkstra 

<hr>

## Algorithm Comparison

![](./assets/BigO.png)

<hr>

### Resources:
* [MIT 6.006](./notes/MIT6006)
* [Stanford CS161](./notes/Stanford%CS161)
* [Real Python: Sorting Algorithms in Python](https://realpython.com/sorting-algorithms-python/)
* [Derrick Sherrill's Python Algorithm Series](https://www.youtube.com/playlist?list=PLc_Ps3DdrcTsizjAG5uMhpoDfhDmxpOzv)
* [Brian Faure's Python Algorithms](https://www.youtube.com/playlist?list=PLEJyjB1oGzx2h88Tj90B5_HadLq339Cso)