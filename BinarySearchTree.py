# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()
'''
BST : left node value is smaller than right value: so search, insert, delete very quickly.
run time of seach in BST is equal height of tree: O(log(n))
insert of BST :               '''
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False
    
##### my add : least common ancestor and binary search tree    
    def questioin4(self, T, r, n1, n2):  
    # Base Case
        make_BST_fm_matrix(T,root,n1,n2)
        n1_ps = []
        while n1 != r:
            print "old n1:",n1
            n1 = exit_parent(T,r,n1)
            print "new n1:",n1
            print"*"*10
            n1_ps.append(n1)
            print "n1_ps: end of while n1 !=1:",n1_ps  
        
        if self.root is None:
            return None
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
        if(self.root.value > n1 and self.root.value > n2):
            return self.questioin4(self.root.left, n1, n2)
    # If both n1 and n2 are greater than root, then LCA
    # lies in right 
        if(self.root.value < n1 and self.root.value < n2):
            return self.questioin4(self.root.right, n1, n2)
        return self.root
    
    def make_BST_fm_matrix(T,root,n1,n2):
        node_list=[]
        numrows = len(T)
        for i in range(numrows):
            if T[i][n1] == 1:
                node_list.append(i)
            if T[i][n2] == 1:
                node_list.append(i)
    
# Set up tree
def exit_parent(T,r,n):
#return parent of n if it exists, otherwise return -1
    numrows = len(T)
    print "matrix_row_size:",numrows
    
    for i in range(numrows):
        print "^^i and T[i][n]:",i, T[i][n]
# In row i(node i) If we found 1 in, stop for loop and  return 0
        if T[i][n] == 1:
            return i  
    return -1


# def make_BST_fm_matrix(T,root,n1,n2):
    
    
tree = BST(3) # root is  3
input_list=[0,3]
# Insert elements
n1= 1
n2= 4
for e in input_list:
    tree.insert(e)
for e in [n1,  n2]:
    tree.insert(e)
# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

##test for least  common ancestor  
  
# root = 3
# n1= 1
# n2= 4
# t=tree.questioin4(root, n1, n2)
#  
# print t.value
# print"LCA of  %d and %d is $d" %(n1, n2, t.value)

##### my add 
question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)



    
# # Set up tree
# tree = BST(4)
# 
# # Insert elements
# tree.insert(2)
# tree.insert(1)
# tree.insert(3)
# tree.insert(5)
# 
# # Check search
# # Should be True
# print tree.search(4)
# # Should be False
# print tree.search(6)

'''Traversal
Main article: Tree traversal

Once the binary search tree has been created, its elements can be retrieved 
in-order by recursively traversing the left subtree of the root node, 
accessing the node itself, then recursively traversing the right subtree of the node,
 continuing this pattern with each node in the tree as it's recursively accessed.
  As with all binary trees, one may conduct a pre-order traversal or 
  a post-order traversal, but neither are likely to be useful for binary search trees. 
  An in-order traversal of a binary search tree will always result in 
  a sorted list of node items (numbers, strings or other comparable items).

The code for in-order traversal in Python is given below. 
It will call callback (some function the programmer wishes to call on 
the node's value, such as printing to the screen) for every node in the tree.

def traverse_binary_tree(node, callback):
    if node is None:
        return
    traverse_binary_tree(node.leftChild, callback)
    callback(node.value)
    traverse_binary_tree(node.rightChild, callback)

Traversal requires O(n) time, since it must visit every node. 
This algorithm is also O(n), so it is asymptotically optimal.

Traversal can also be implemented iteratively. 
For certain applications, e.g. greater equal search, approximative search,
 an operation for single step (iterative) traversal can be very useful.
  This is, of course, implemented without the callback construct and 
  takes O(1) on average and O(log n) in the worst case.'''
  
  
'''# Python program to do inorder traversal without recursion
 
# A binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
# Iterative function for inorder tree traversal
def inOrder(root):
     
    # Set current to root of binary tree
    current = root 
    s = [] # initialze stack
    done = 0
     
    while(not done):
         
        # Reach the left most Node of the current Node
        if current is not None:
             
            # Place pointer to a tree node on the stack 
            # before traversing the node's left subtree
            s.append(current)
         
            current = current.left 
 
         
        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is 
        # empty you are done
        else:
            if(len(s) >0 ):
                current = s.pop()
                print current.data,
         
                # We have visited the node and its left 
                # subtree. Now, it's right subtree's turn
                current = current.right 
 
            else:
                done = 1
 
# Driver program to test above function
 
""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
inOrder(root)'''
#################### abovee  explanation : time complexity O(N)

# Inorder Tree Traversal without Recursion
# 
# Using Stack is the obvious way to traverse tree without recursion. Below is an algorithm for traversing binary tree using stack. See this for step wise step execution of the algorithm.
# 
# 1) Create an empty stack S.
# 2) Initialize current node as root
# 3) Push the current node to S and set current = current->left until current is NULL
# 4) If current is NULL and stack is not empty then 
#      a) Pop the top item from stack.
#      b) Print the popped item, set current = popped_item->right 
#      c) Go to step 3.
# 5) If current is NULL and stack is empty then we are done.
# 
# Let us consider the below tree for example
# 
#             1
#           /   \
#         2      3
#       /  \
#     4     5
# 
# Step 1 Creates an empty stack: S = NULL
# 
# Step 2 sets current as address of root: current -> 1
# 
# Step 3 Pushes the current node and set current = current->left until current is NULL
#      current -> 1
#      push 1: Stack S -> 1
#      current -> 2
#      push 2: Stack S -> 2, 1
#      current -> 4
#      push 4: Stack S -> 4, 2, 1
#      current = NULL
# 
# Step 4 pops from S
#      a) Pop 4: Stack S -> 2, 1
#      b) print "4"
#      c) current = NULL /*right of 4 */ and go to step 3
# Since current is NULL step 3 doesn't do anything. 
# 
# Step 4 pops again.
#      a) Pop 2: Stack S -> 1
#      b) print "2"
#      c) current -> 5/*right of 2 */ and go to step 3
# 
# Step 3 pushes 5 to stack and makes current NULL
#      Stack S -> 5, 1
#      current = NULL
# 
# Step 4 pops from S
#      a) Pop 5: Stack S -> 1
#      b) print "5"
#      c) current = NULL /*right of 5 */ and go to step 3
# Since current is NULL step 3 doesn't do anything
# 
# Step 4 pops again.
#      a) Pop 1: Stack S -> NULL
#      b) print "1"
#      c) current -> 3 /*right of 5 */  
# 
# Step 3 pushes 3 to stack and makes current NULL
#      Stack S -> 3
#      current = NULL
# 
# Step 4 pops from S
#      a) Pop 3: Stack S -> NULL
#      b) print "3"
#      c) current = NULL /*right of 3 */  
# 
# Traversal is done now as stack S is empty and current is NULL. 
  
  
  