# -*- coding: utf-8 -*-
'''
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is 
the farthest node from the root that is an ancestor of both nodes. For example, the root is a common 
ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that 
left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the 
tree itself adheres to all BST properties. The function definition should look like 
"question4(T, r, n1, n2)", where T is the tree represented as a matrix, where the index of the list is 
equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer 
representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular 
order. For example, one test case might be 
question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4), and the answer would be 3.
'''
# class Node:
#  
#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
      
         
def question4(T, root, n1, n2):
    done = 0
    while(not done):
        if n1<root and root <= n2:  #check whether it is balanced tree, if so, root is common ancestor of n1,n2
            return root
            done = 1
        else : #otherwise(unbalanced), left traversal
            for i in xrange(len(T)): #It is binary search tree,where left child < root <= right child.   
                if T[root][i] == 1:                    
                    if i <  root : 
                        root = i                       
                        break
                    
                         
                      
                
       
# def question4(T, root, n1, n2):
#     if n1<root and root <= n2:  #check whether it is balanced tree, if so, root is common ancestor of n1,n2
#         return root
#     else : #otherwise(unbalanced), left traversal
#         for i in xrange(len(T)): #It is binary search tree,where left child < root <= right child.    
#             if T[root][i] == 1: #Find only first element of  which element is 1, is left child and  it become new root and stop for  loop.                 
#                 root= i              
#                 break       
#         return question4(T, root, n1, n2)  



print "test 1:",question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
# test 1: 3
print "test 2:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,2,5)
# test 2: 3
print "test 3:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,0,2)
# test 3: 1
print "test 4:",question4([[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0]],0,5,6) 
#test 4: 6  :error should be 5