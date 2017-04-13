# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()

'''If we are given a BST(Binary Search Tree) where every node has parent pointer, 
then LCA can be easily determined by traversing up using parent pointer 
and printing the first intersecting node.

We can solve this problem using BST properties. 
We can recursively traverse the BST from root. 
The main idea of the solution is, while traversing from top to bottom, 
the first node n we encounter with value between n1 and n2, i.e., n1 < n < n2 
or same as one of the n1 or n2, is LCA of n1 and n2 (assuming that n1 < n2). 
So just recursively traverse the BST in, if node�s value is greater than 
both n1 and n2 then our LCA lies in left side of the node, 
if it�s is smaller than both n1 and n2, then LCA lies on right side. 
Otherwise root is LCA (assuming that both n1 and n2 are present in BST)
'''
# A recursive python program to find LCA of two nodes
# n1 and n2
 
# A Binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def question4(T,root, n1, n2):
 
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
#     if root is  None:
#         return  None
#     
#     if(root.data > n1 and root.data > n2):
#         return questioin4(root.left, n1, n2)
#  
#     # If both n1 and n2 are greater than root, then LCA
#     # lies in right 
#     if(root.data < n1 and root.data < n2):
#         return questioin4(root.right, n1, n2) 

#     return root
    root = Node(root)
#     make_bst(T,root,n1,n2)
#     root = Node(root)
    while(root!= None):
        make_bst(T,root,n1,n2)
        if root.data >n1 and root.data > n2:   #left traverse
            root = root.left
            print "** 1st root while:",root
        elif root.data < n1 and root.data < n2:  #right  traverse
            root = root.right
            print "^^ 2nd root  while:",root
        else:                     # when n1 < root <= n2 ,  lca is root 
            break
    return root    
            
        
def make_bst(T,root,n1,n2):
#     root = Node(root)
    for i in xrange(len(T)): #It is binary search tree,where left child < root <= right child.   
        if T[root.data][i] == 1:  #root: current root node, i : child node
            if i < root.data: #left child
                root.left  = Node(i)
#                 root = root.left
                print "%% below root.left:", Node(i).data
#                 root  = Node(i)
#                 print "%% below root.left:", Node(i).data
            else :
                root.right = Node(i)
#                 root = root.right
                print "%% below root.right:", Node(i).data
#                 root = Node(i)
#                 print "%% below root.right:", Node(i).data
                
            
            
    
print "test 1:",question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
# test 1: 3
print "test 2:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,2,5)
# test 2: 3
print "test 3:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,0,2)
# test 3: 1
print "test 4:",question4([[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0]],0,5,6) 
#test 4: 6  :error should be 5    

# def find_child(T,r,n1,n2):
#     for i in T[i]    # row 3:[1 0 0 0 1] -> root:3, left child:0(index 0),  right child:4(index 4)
#     
 #return parent of n if it exists, otherwise return -1
# def exit_parent(T,n):
#     size_of_rows = len(T)
#     print  "matrix_row_col_size :",size_of_rows
#     #for  each  node, i
#     for  i in  range(size_of_rows):
#         print "^^ T [i and n]:",T[i][n]
# the index of the list is equal to the integer stored in 
# that node and a 1 represents a child node        
#         if T[i][n] == 1:
#             return i
#     return  -1

# def make_bst_node(T,r,n1,n2):  #To do but it is implemented in BinarySearchTree.py
#     size_of_rows = len(T)
#     root = Node(r)
#     for i in range(size_of_rows):
#         if T[r][i]==1:  #i is child of  r
#             if i < r:  #child  is  less than root, connect it as left child.
#                 root.left = Node(i)
#             else:    
#                 root.right = Node(i)
                
     
    
    

# print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
 
# Driver program to test above function


########################################################################
  
# Let us construct the BST shown in the figure
# root = Node(20)
# root.left = Node(8)
# root.right = Node(22)
# root.left.left = Node(4)
# root.left.right = Node(12)
# root.left.right.left = Node(10)
# root.left.right.right = Node(14)
#    
#   
# n1 = 10 ; n2 = 14
# t = questioin4(root, n1, n2)
# print "LCA of %d and %d is %d" %(n1, n2, t.data)
#    
# n1 = 14 ; n2 = 8
# t = questioin4(root, n1, n2)
# print "LCA of %d and %d is %d" %(n1, n2 , t.data)
#    
# n1 = 10 ; n2 = 22
# t = questioin4(root, n1, n2)
# print "LCA of %d and %d is %d" %(n1, n2, t.data)
  

# tree = BST(3) # root is  3
# input_list=[0,3]
# # Insert elements
# n1= 1
# n2= 4
# for e in input_list:
#     tree.insert(e)
# for e in [n1,  n2]:
#     tree.insert(e)
# # Check search
# # Should be True
# print tree.search(4)
# # Should be False
# print tree.search(6)
# 
# ##test for least  common ancestor  
#   
# root = 3
# n1= 1
# n2= 4
# t=tree.questioin4(root, n1, n2)
#  
# print t.value
