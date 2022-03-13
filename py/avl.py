# RUN: python dsa/py/avl.py

"""
AVL Tree implementation

BST Interface Methods
* insert
* search
* in_order
* pre_order
* post_order
* delete
"""

from bst import BST
from queue import Queue

class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None
        self.length = 0

    def __len__(self):
        return self.length

    def height(self, node):
        if node:
            return node.height
        else:
            return 0
     
    def skew(self, node):
        if node:
            return self.height(node.right) - self.height(node.left)
        else:
            return 0

    def update(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))    

    def rotate_right(self,D): # O(1)
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.val, B.val = B.val, D.val
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A: A.parent = B
        if E: E.parent = D
        self.update(B)
        self.update(D)
    
    def rotate_left(self, B): # O(1)
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.val, D.val = D.val, B.val
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A: A.parent = B
        if E: E.parent = D
        self.update(B)
        self.update(D)
    
    def rebalance(self, node): # O(1) 
        if self.skew(node) == 2: 
            if self.skew(node.right) < 0: 
                self.rotate_right(node.right) 
                self.rotate_left(node) 
            elif self.skew(node) == -2: 
                if self.skew(node.left) > 0: 
                    self.rotate_left(node.left) 
                    self.rotate_right(node)
    
    def maintain(self, node):
        self.rebalance(node)
        self.update(node)
        if node.parent:
            self.maintain(node.parent)

    def insert(self, val):
        node = Node(val)
        # If empty tree
        if self.root is None:
            self.root = node
            print(f'Set root to {node.val}.')
        else:
            # Search for val
            x = self.search(val=val, root_node=self.root)
            # If already exists
            if x.val == val:
                print(f"Node {val} already exists")
                return x
            # Else, x is parent node
            node.parent = x
            # Assume from search that parent has blank left/right child
            if val < x.val:
                x.left = node
            else:
                x.right = node
            
        self.length += 1
        self.maintain(node) # rebalance tree
        return node

    def search(self, val, root_node=None):
        """
        Recursively find the node with value val, if exists in tree
        Return node and level it exists on
        """
        if root_node is None:
            root_node = self.root
        if root_node.val == val:
            print(f'Found node {val}.')
            return root_node
        # If val < root_node, take subtree of child.left
        elif val < root_node.val:
            if root_node.left is None:
                print(f'No node {val}. Parent node is {root_node.val}.')
                return root_node
            else:
                return self.search(val, root_node.left)
        # If val > root_node, take subtree of child.right
        elif val > root_node.val:
            if root_node.right is None:
                print(f'No node {val}. Parent node is {root_node.val}.')
                return root_node
            else:
                return self.search(val, root_node.right)
        
    
    def in_order(self, node=None, nodes=[]):
        """
        Traverse in direction of smallest to largest
        """
        if node is None:
            node = self.root
        # Traverse child.left as deep as possible
        if node.left is not None:
            self.in_order(node.left, nodes)
        # If we are as far left (smallest value) as possible, append node
        nodes.append(node)
        # Traverse child.right as deep as possible
        if node.right is not None:
            self.in_order(node.right, nodes)
        
        return nodes
    
    def min_node(self, node):
        """
        Recursively moves down to the furthest left node 
        """
        if node.left is None:
            return node
        else:
           return self.min_node(node.left)
    
    def get_parent(self, node):
        """
        Recursively moves up heirarchy
        """
        print("parent loops")
        if node.val < node.parent.val:
            return node.parent
        else:
            return self.get_parent(node.parent)

    def next_node(self,node):
        # If right subtree
        if node.right is not None:
            return self.min_node(node.right)
        # Otherwise, move up ancestory until right subtree exists
        else:
            return self.get_parent(node)
     
    def delete(self,node):
        """
        Only subtract from length in the non-recursive cases (0,1 children)
        """
        if node is not None:
            # --- 0 Children ----
            if (node.left is None) and (node.right is None):
                # 0a: node is a single root node (no parent)
                if self.root == node:
                    self.root = None
                # 0b: has parent node
                elif node.val < node.parent.val:
                    node.parent.left = None
                elif node.val > node.parent.val:
                    node.parent.right = None
                else:
                    raise Exception("Delete Error")
                
                self.length -= 1
            
            # --- 1 Children ----
            if (node.right is None and node.left is not None) or (node.left is None and node.right is not None):
                # Get child
                if node.left is not None:
                    child = node.left
                else:
                    child = node.right
                # If node is root node, set to child
                if self.root == node:
                    self.root = child
                # Point node.parent at child
                if node == node.parent.left:
                    node.parent.left = child
                else:
                    node.parent.right = child
                # Point child at node.parent
                child.parent = node.parent
                
                self.length -= 1

            # --- 2 Children ----
            if (node.right is not None) and (node.left is not None):
                # find the successor = left most child in the right sub tree
                nxt = self.next_node(node)
                # Assign value
                node.val = nxt.val
                # Recursively delete successor (relocated) node
                self.delete(nxt)

            self.maintain(node.parent) # rebalance tree

        else:
            print("Cannot delete. Node not in BST")

    def level_order(self):
        nodes=[]
        q=Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            node = q.dequeue()
            nodes.append(node)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

        return nodes

def main():
    # Build tree
    avl = AVL()
    bst =BST()
    for i in [6,3,8,5,2,7,2,11,9,10,13]:
        avl.insert(i)
        bst.insert(i)

    print(f'length {len(avl)}')
    print(f'length {len(bst)}')

    # Compare BST and AVL
    print("BST")
    print(f'In Order: {[node.val for node in bst.in_order()]}')
    print(f'Level Order: {[node.val for node in bst.level_order()]}')
    # BST looks like this
    #      6
    #    /   \
    #   3     8
    #  / \   / \
    # 2   5 7   11
    #          /  \
    #         9    13
    #          \
    #           10
    print("AVL")
    in_order = avl.in_order()
    print(f'In Order: {[(node.val, node.height) for node in in_order]}')
    print(f'Level Order: {[node.val for node in avl.level_order()]}')
    # AVL looks like this
    #      6
    #    /   \
    #   3     9
    #  / \   / \
    # 2   5 8   11
    #      /   /  \
    #     7   10   13

    y = avl.search(9)
    avl.delete(y)
    print(f'AVL Level Order: {[node.val for node in avl.level_order()]}')
    # New AVL looks like this
    #      6
    #    /   \
    #   3     10
    #  / \   /  \
    # 2   5 8   11
    #      /      \
    #     7        13

if __name__ == "__main__":
    main()

"""
OUTPUT
BST
    In Order: [2, 3, 5, 6, 7, 8, 9, 10, 11, 13]
    Level Order: [6, 3, 8, 2, 5, 7, 11, 9, 13, 10]
AVL
    In Order: [(2, 1), (3, 2), (5, 1), (6, 4), (7, 1), (8, 2), (9, 3), (10, 1), (11, 2), (13, 1)]
    Level Order: [6, 3, 9, 2, 5, 8, 11, 7, 10, 13]
Found node 9.
AVL Level Order: [6, 3, 10, 2, 5, 8, 11, 7, 13]
"""