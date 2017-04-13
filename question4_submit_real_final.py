# -*- coding: utf-8 -*-

# A Binary tree node
class Node: 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def question4(T,root, n1, n2):
    root = Node(root)
    while(root!= None):
        make_bst(T,root,n1,n2)
        if root.data >n1 and root.data > n2:   #left traverse
            root = root.left
        elif root.data < n1 and root.data < n2:  #right  traverse
            root = root.right
        else:                     # when n1 < root <= n2 ,  lca is root 
            break
    return root.data    
                  
def make_bst(T,root,n1,n2):
#     root = Node(root)
    for i in xrange(len(T)): #It is binary search tree,where left child < root <= right child.   
        if T[root.data][i] == 1:  #root: current root node, i : child node
            if i < root.data: #left child
                root.left  = Node(i)
            else :
                root.right = Node(i)
                         
print "test 1:",question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
# test 1: 3
print "test 2:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,2,5)
# test 2: 3
print "test 3:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,0,2)
# test 3: 1
print "test 4:",question4([[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0]],0,5,6) 
# test 4: 5
print "test 5:",question4([[0,0,0,0,0,0,0],[1,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,0,0,1,0],[0,0,0,0,0,0,0],[0,0,0,0,1,0,1],[0,0,0,0,0,0,0]],3,4,6)
# test 5: 5 