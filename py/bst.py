# RUN: python py/bst.py

"""
Binary Search Tree implementation

BST Interface Methods
* insert
* find
* in_order
* pre_order
* post_order
* delete
"""

from queue import Queue

class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None
        self.length = 0

    def __len__(self):
        return self.length
   
    def insert(self, val):
        node = Node(val)
        # If empty tree
        if self.root is None:
            self.root = node
            self.length += 1
        else:
            self._insert(self.root, node)

    def _insert(self, root_node, node):
        # Recursively divide into subtrees of root_node & child.left, child.right
        # If value already exists, return it
        if root_node.val == node.val:
            return root_node
        if node.val < root_node.val:
            # If already child.left, recurse along left branch
            if root_node.left is not None:
                self._insert(root_node.left, node)
            else:
                # If node is now a leaf, assign node
                self.length +=1
                root_node.left = node
                node.parent = root_node
        # If node > parent value
        elif node.val > root_node.val:
            # If already child.right, recurse along right branch
            if root_node.right is not None:
                self._insert(root_node.right, node)
            else:
                # If node is now a leaf, assign node
                self.length +=1
                root_node.right = node
                node.parent = root_node

    def find(self, val, root_node=None, lvl=0):
        """
        Recursively find the node with value val, if exists in tree
        Return node and level it exists on
        """
        if root_node is None:
            root_node = self.root
        if root_node.val == val:
            print(f'Found node {val}.Node level = {lvl}')
            return root_node
        # If val < root_node, take subtree of child.left
        elif val < root_node.val:
            lvl +=1
            try:
                return self.find(val, root_node.left, lvl)
            except:
                print(f'{val} does not exist in BST')
        # If val > root_node, take subtree of child.right
        elif val > root_node.val:
            lvl +=1
            try:
                return self.find(val, root_node.right, lvl)
            except:
                print(f'{val} does not exist in BST')
        
        # Or can returns would-be parent if value does not exist
        return None
    
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

    def pre_order(self, node=None, nodes=[]):
        """
        Traverse root -> left -> right
        """
        if node is None:
            node = self.root
        # Append parent node
        nodes.append(node)
        # Traverse child.left as deep as possible
        if node.left is not None:
            self.pre_order(node.left, nodes)
        # Traverse child.right as deep as possible
        if node.right is not None:
            self.pre_order(node.right, nodes)
        
        return nodes

    def post_order(self, node=None, nodes=[]):
        """
        Traverse left -> right --> root
        """
        if node is None:
            node = self.root
        # Traverse child.left as deep as possible
        if node.left is not None:
            self.post_order(node.left, nodes)
        # Traverse child.right as deep as possible
        if node.right is not None:
            self.post_order(node.right, nodes)
        # Append parent node
        nodes.append(node)
        
        return nodes
     
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
        else:
            print("Cannot delete. Node not in BST")


def main():
    # Build tree
    bst = BST()
    for i in [6,3,8,5,2,7,2,11, 9,10,13]:
        bst.insert(i)

    print(f'length {len(bst)}')

    # Tree should look like this
    #      6
    #    /   \
    #   3     8
    #  / \   / \
    # 2   5 7   11
    #          /  \
    #         9    13
    #          \
    #           10

    # Demo traversal methods
    in_order = bst.in_order()
    print(f'In Order: {[node.val for node in in_order]}')
    pre_order = bst.pre_order()
    print(f'Pre Order: {[node.val for node in pre_order]}')
    post_order = bst.post_order()
    print(f'Post Order: {[node.val for node in post_order]}')
    level_order = bst.level_order()
    print(f'Level Order: {[node.val for node in level_order]}')
  
    bst.delete(bst.find(9))
    print(f'Level Order: {[node.val for node in bst.level_order()]}')
    bst.delete(bst.find(20))
    bst.delete(bst.find(13))
    bst.delete(bst.find(6))
    print(f'Level Order: {[node.val for node in bst.level_order()]}')
    
    print(f'length {len(bst)}')


if __name__ == "__main__":
    main()


"""
OUTPUT
length 10
In Order: [2, 3, 5, 6, 7, 8, 9, 10, 11, 13]
Pre Order: [6, 3, 2, 5, 8, 7, 11, 9, 10, 13]
Post Order: [2, 5, 3, 7, 10, 9, 13, 11, 8, 6]
Level Order: [6, 3, 8, 2, 5, 7, 11, 9, 13, 10]
Found node 9.Node level = 3
Level Order: [6, 3, 8, 2, 5, 7, 11, 10, 13]
20 does not exist in BST
Cannot delete. Node not in BST
Found node 13.Node level = 3
Found node 6.Node level = 0
Level Order: [7, 3, 8, 2, 5, 11, 10]
length 7
"""