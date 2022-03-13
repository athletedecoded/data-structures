# Dynamic Programming

* Dynamic Programming is about reducing the problem space to constant-size subproblems
* Paradigm which combines recursion and memoization (i.e. solutions held in memory) 
* General structure
    ```
    def dp_fxn(*args, **kwargs):
        # Instantite memo to store {subproblem:solution} pairs within function scope
        memo = dict()
        # Define the subproblem fxn
        def F(i):
            # Is this the base case?
            if i == base_case: 
                return i
            # Solve this problem if we haven't
            if i not in memo:
                memo[i] = F(sub1) <relation> F(sub2)
            # Else return the solution
            return memo[i]
        return F(n)
    ```

## SRTBOT Framework

* **Subproblem:** Define the problem for arbitrary ith subproblem
* **Relation:** How are the subproblems related to each other 
* **Topo Sort:** Topographical order to solve the subproblems 
* **Base Case:** Define the base case (beware the infinite loop!) 
* **Original:** Write the original problem in terms of the subproblem 
* **Time:** Complexity analysis


<hr>

### Resources:
* [Stanford CS161 Lesson 13](./notes/StanfordCS161/13%20DP-II.pdf)
* [William Fiset's Dynamic Programming](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u)
* [Reducible Dynamic Programming](https://www.youtube.com/watch?v=aPQY__2H3tE)
* [FCC Dynamic Programming](https://www.youtube.com/watch?v=oBt53YbR9Kk)