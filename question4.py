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
    n1_ps = []
    while n1 != r:
        print "old n1:",n1
        n1 = parent(T, n1)
        print "new n1:",n1
        print"*"*10
        n1_ps.append(n1)
    print "n1_ps: end of while n1 !=1:",n1_ps    
    print "len(n1_ps):",len(n1_ps)
    if len(n1_ps) == 0:  #if n1 is root return -1
        return -1
    while n2 != r:
        print "$$ old n2:",n2
        n2 = parent(T, n2)
        print "$$ new n2:",n2
        print "$$ n1_ps :",n1_ps
# if n2 and n1 has common ancestor
        if n2 in n1_ps:
            return n2
    return -1
    
    
def parent(T, n):
    #return parent of n if it exists, otherwise return -1
    numrows = len(T)
    print "matrix_row_size:",numrows
    for i in range(numrows):
        print "^^i and T[i][n]:",i, T[i][n]
        if T[i][n] == 1:
            return i  #ex) i=0 found 1 in T[i][n] stop for loop and  return 0
    return -1


print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
