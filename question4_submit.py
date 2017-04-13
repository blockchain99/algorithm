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

def question4(T, r, n1, n2):
    n1_list = []
    #while node n1 is not equal to root
    while n1 != r:
        #return n1's parent node, which was row number of matrix with 1.
        n1 = exist_parent(T, n1)
        n1_list.append(n1)

    if len(n1_list) == 0:  #if n1 is root return -1
        return -1
    while n2 != r:
        n2 = exist_parent(T, n2)
# if n2 and n1 has common ancestor, return n2
        if n2 in n1_list:
            return n2
    return -1
    
#for each node(row) and column with given node(n1 or  n21), if it  is 1, return each node(row)
# otherwise return -1    
def exist_parent(T, n):
    numrows = len(T)
    for i in range(numrows):
        if T[i][n] == 1:
            return i  #For example, i=0 found 1, stop for-loop and  return 0
    return -1

print "test 1:",question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
# test 1: 3
print "test 2:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,2,5)
# test 2: 3
print "test 3:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,0,2)
# test 3: 1

