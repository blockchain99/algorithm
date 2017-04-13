# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()
''' Trees(root, node, vertical connection): 
not cycles(count same node twice, such as connection to the root), no unconnected node,
height -reverse relationship- depth
                        (root(A), height:3, depth:0)                    - level 1 (all parent)-root
                          /                    \
            (node(B), height:2, depth:1)  (node(C), height:2, depth:1)  - level 2,(parent and child)-intermediate node      
                 /                \             /               \
     (node(D),height:0, depth:2)(node(E))  (node(F))          (node(G)) - level 3,(all child)-leaf   '''
     
'''BFS(Bredth First Search) Level Order: A,/ B, C/,D,E,F,G/, 
 DFS(Depth First search)   : 
  1) pre-order approach(check-up children node before traverse):A,B,D,E,C,F,G
  2) iN-ORDER approach (traverse left children first, if no left child traverse to parent)
    - start at traversing down left to leaf. check up the leaf and move up to parent, then right child who has no left child(leaf)
    :D,B,E,A,F,C,G
  3) Post-order traversal (all leaf(child) checkup first then checkup parent): D,E,B,F,G,C,A  '''
#  D, F, E, B, C, A 
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.children = None
# 
# 
# class Tree:
#     def __init__(self, root=None):
#         self.root = root
        
''' create your own binary tree 
Every node has some value, and pointers to left and right children. 

You'll need to implement two methods: search(), which searches for the presence of 
a node in the tree, and print_tree(), which prints out the values of tree nodes in 
a pre-order traversal. You should attempt to use the helper methods provided 
to create recursive solutions to these functions. 
'''        
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
#         """Return True if the value
#         is in the tree, return
#         False otherwise."""
#         return False
        return self.preorder_search(tree.root, find_val)
    
    def print_tree(self):
#         """Print out all tree nodes
#         as they are visited in
#         a pre-order traversal."""
#         return ""
        return self.preorder_print(tree.root, "")[:-1]
    
    def preorder_search(self, start, find_val):
#         """Helper method - use this to create a 
#         recursive search solution."""
#         return False
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False
    
    def preorder_print(self, start, traversal):
#         """Helper method - use this to create a 
#         recursive print solution."""
#         
#         return traversal
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()       