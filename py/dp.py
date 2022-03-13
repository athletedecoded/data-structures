# RUN: python py/dp.py

"""
Dynamic Programming Examples
1) Nth Fibonacci Number
2) 0/1 Knapsack
3) Longest Common Subsequence
"""
# -----------------------------------------------
# Nth Fibonacci number
def fib(n):
    """
    Given n (int), compute the nth fibonacci number using DP
    """
    # Subproblem: ith fibonacci number, F(i) for [1:n]
    # Relation: F(i) = F(i-1) + F(i-2)
    # Topo: i=1 to i=n
    # Base: F(1) = F(2) = 1
    # Original: F(n) = F(n-1) + F(n-2) for n

    # Instantite memo to store {n:F(n)} pairs
    memo = dict()
    # Define the subproblem case
    def F(i):
        # Is this the base case?
        if i < 2: 
            return i
        # Define subproblem relation
        if i not in memo:
            memo[i] = F(i - 1) + F(i - 2)
        return memo[i]
    return F(n)

# -----------------------------------------------
# 2. 0-1 Knapsack
def knapsack(items, capacity):
    # Generate init value table
    n = len(items)
    K = [[None]*(capacity + 1) for _ in range(n+1)]
    # Zero first column
    for i in range(n+1):
        K[i][0] = 0
    # Zero first row
    for c in range(capacity + 1):
        K[0][c] = 0
    # Build value table
    for i in range(1,n+1):
        # Current item val and weight
        w = items[i]['wt']
        v = items[i]['val']
        for c in range(1,capacity + 1):
            # curr best at this capacity = row above, same column
            K[i][c] = K[i-1][c]
            # if item weight < capacity
            if w <= c: 
                K[i][c] = max(K[i][c], K[i-1][c-w] + v)
    # Select items
    selected = []
    W = capacity
    for i in range(n, 0, -1):
        if K[i][W] != K[i-1][W]:
            selected.append(i)
            W -= items[i]['wt']

    print(f'For capacity = {capacity}, the best value is {K[n][capacity]} by selecting:')
    for item in selected:
        print(f"Item {item}: wt = {items[item]['wt']}, val = {items[item]['val']}")

# -----------------------------------------------
# 3. Longest Common Substring
def LCS(A,B):
    # Generate init value table: A,m = rows, B,n = cols
    m = len(A)
    n = len(B)
    C = [[None]*(n+1) for _ in range(m+1)]
    # Zero first column
    for i in range(m+1):
        C[i][0] = 0
    # Zero first row
    for i in range(n+1):
        C[0][i] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            # If letter match, increment length of previous longest
            if A[i-1] == B[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                # Get current longest from memory
                C[i][j] = max(C[i-1][j], C[i][j-1])
    # Get the substring
    longest = []
    i, j = m-1,n-1
    while i >= 0 and j >= 0:
        if A[i] == B[j]:
            longest.append(A[i])
            i -= 1
            j -= 1
        elif C[i][j] == C[i][j-1]:
            j -= 1
        else:
            i -= 1
    longest.reverse()
    substr = "".join(longest)
    print(f'The longest common substring of {A} and {B} is "{substr}"')

# -----------------------------------------------


if __name__ == "__main__":
    print("First 10 fibonacci numbers")
    nums = []
    for x in range(10):
        nums.append(fib(x))
    print(nums)
    print("---------------------------------")
    print("The 0/1 Knapsack Problem")
    items = {1: {'val':2,'wt':3},
        2: {'val':2,'wt':1},
        3: {'val':4,'wt':3},
        4: {'val':5,'wt':4},
        5: {'val':3,'wt':2}}
    knapsack(items,5)
    knapsack(items,12)
    print("---------------------------------")
    print("The LCS Problem")   
    LCS("hello", "yellow")
    LCS("dangerous", "pancakes")
    LCS("ADECECDCDCCECDC", "DDECEDCACADEDCED")
    print("---------------------------------")

"""
OUTPUT
First 10 fibonacci numbers
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
---------------------------------
The 0/1 Knapsack Problem
For capacity = 5, the best value is 7 by selecting:
Item 4: wt = 4, val = 5
Item 2: wt = 1, val = 2
For capacity = 12, the best value is 14 by selecting:
Item 5: wt = 2, val = 3
Item 4: wt = 4, val = 5
Item 3: wt = 3, val = 4
Item 1: wt = 3, val = 2
---------------------------------
The LCS Problem
The longest common substring of hello and yellow is "ello"
The longest common substring of dangerous and pancakes is "ans"
The longest common substring of ADECECDCDCCECDC and DDECEDCACADEDCED is "DECEDCCDC"
"""