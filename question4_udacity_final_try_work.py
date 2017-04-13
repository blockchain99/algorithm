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
def question4(T, root, n1, n2):
#     done = 0
#     while(not done):
    weight_count = 0
    length = 6
    print "* lengh :",length
     # Set current to root of binary tree
    current = Node(root) 
    s = []  #stack LIFO for left  node
    s2 = []
    q = [] #queue for FIFO for right  node
    
    done = 0
   
#     while True:   #need break
    while  length >1 :   
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
        print "*"
        if n1<current.data and current.data <= n2:  #check whether it is balanced tree, if so, root is common ancestor of n1,n2
            print "answer current",current.data
            return current.data
            length =- 1
        else :
            if(current.data > n1 and current.data > n2):
                print "parent_current:",current.data
                for i in xrange(len(T)):    
                    if T[current.data][i] == 1:  #1 , 3 
#               return questioin4(current.left, n1, n2)
#                         print "children.data:",current.data
                        current.left= Node(i)  
                        
#                         print "current. before left",current.left.data                    
                        s.append(current.left)
#                         current = current.left  
                        
#                         print "current after left:",current.data
                current.left=s.pop(0)    #first pop of FIFO , 1
                print "current",current.data
                print "s.data :it  shows None?",current.left.data  #1
#                 print "s.data2 :",s.pop().data #empty list  error
#                 current.left=s.pop(0) #queue FIFO   2nd pop(0) 5 
#                 current = current.left

                length =- 1
                
                print "length :",length
#                 print "current.data in left:",current.data
    # If both n1 and n2 are greater than root, then LCA
    # lies in right 
#             if(current.data < n1 and current.data < n2):
#                 for i in xrange(len(T)):
#                     if T[current.data][i] == 1:
# #               return questioin4(current.left, n1, n2)
#                         current = Node(i)
# #                         current = current.right 
#                         print "current.data_right:",current.data    
#                 length =- 1
#                 print "length  right:",length

'''Lifo                
stack = list()
stack.append(1)
stack.append(2)
stack.append(3)

print stack.pop()  #3
print stack.pop()  #2
print stack.pop()  #1

For a FIFO use the index 0 for the first element:
stack = list()
stack.append(1)
stack.append(2)
stack.append(3)

print stack.pop(0)  #1
print stack.pop(0)  #2
print stack.pop(0)  #3'''

# def find_child(T,r,n1,n2):
#     for i in T[i]    # row 3:[1 0 0 0 1] -> root:3, left child:0(index 0),  right child:4(index 4)
#     

# def make_bst_node(T,r,n1,n2):  #To do but it is implemented in BinarySearchTree.py
#     size_of_rows = len(T)
#     root = Node(r)
#     for i in range(size_of_rows):
#         if T[r][i]==1:  #i is child of  r
#             if i < r:  #child  is  less than root, connect it as left child.
#                 root.left = Node(i)
#             else:    
#                 root.right = Node(i)
                
     
# print "test 1:",question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
# # test 1: 3
# print "test 2:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,2,5)
# test 2: 3
print "test 3:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,0,2)
# test 3: 1
# print "test 4:",question4([[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0]],0,5,6) 
# #test 4: 6  :error should be 5    
#     

# print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
 
# Driver program to test above function
  
# # Let us construct the BST shown in the figure
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
