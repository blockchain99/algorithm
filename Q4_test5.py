'''
Created on Dec 10, 2016

@author: ys
'''

# root = 0
# T= [[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0]]
# for i in xrange(len(T)): #It is binary search tree,where left child < root <= right child.   
#                 if T[root][i] == 1:                    
#                     if i <  root : 
#                         root = i
#                         print "upper if root_i:",i                       
#                         break
#                 else:
#                         root = i
#                         print "else root_i :",root

def question4(T, root, n1, n2):
    done = 0
    
    count  = 0
    while(not done):
        if n1<root and root <= n2:  #check whether it is balanced tree, if so, root is common ancestor of n1,n2
            
            print "--upper before root:",root
            return root
            print "---upper most root:",root
            done = 1
            
        else : #otherwise(unbalanced), left traversal
            count +=1
            print "count:",count
            for i in xrange(len(T)): #It is binary search tree,where left child < root <= right child.            
                if T[root][i] == 1: 
                    if i < root:     
                        root.left  = i
                        root = root.left
                    else:
                        root.right = i
                        root = root.right
                        
                                          
                        
                        
                    
print "test 4:",question4([[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0]],0,5,6) 
#test 4: 6  :error should be 5            

# print "test 3:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,0,2)
# # test 3: 1      