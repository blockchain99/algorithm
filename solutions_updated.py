# -*- coding: utf-8 -*-
'''Question 1 :
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and 
return a boolean True or False.'''

def Question1(s, t):
    s_length = len(s)
    t_length = len(t)
#comparing iteration number is 1st string with - string +1
    for i in range(s_length - t_length + 1): #for example) udacity, ad : 7-2+1=6
#compare the same size of sorted substring of 1st string with 2nd sorted string 
#if there is the same sorted substring in 1st string with 2nd sorted string, return True
#else stay False
        if sorted(s[i: i+t_length])==sorted(t): #ex. t='ad'(2), s[0:2]==t, x[1,3]==t, x[2,4]==t,x[3,5]==t,x[4,6]==t,x[5,7]==t
            return True
    return False


print 'Test 1 : udacity, ad \n',Question1("udacity", "ad")
#Test 1 : udacity, ad 
# True
print 'Test 2 : udacity, tyciuda \n',Question1("udacity", "tyciuda")
# Test 2 : udacity, tyciuda 
# True
print 'Test 3 : timeline, k s \n',Question1("timelne", "k s")
# Test 3 : timeline, k s 
# False
print 'Test 4 : butterfly, a rl \n',Question1("butterfly", "a r")
# Test 4 : butterfly, a rl 
# False


""" Question 2 :
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like "question2(a)", and return a string.
"""

def question2(a):
    a = a.lower()
    #check the forward string from start with the backward string from end
    def is_palindrome(a):   #returns T/F
        return str(a) == str(a)[::-1]
    #Initialize logest_plaindrome with ""
    longest_palindrome = ""
    
    #a[0:1],first logest_plandrome is lengths 1:
    i = 0
    j = 1

    #new value can't be longest_palindrome if len(string[i:j]) <= len(longest palindrome)
    while i < (len(a) - len(longest_palindrome)):
        #the length of palindrome string can't be over the length of input string
        #j is the end positin of palindrome string.
        if j <= len(a):
            temp_string = a[i:j]
            #only worth checking if it is eligible to be the longest 
            if len(temp_string) > len(longest_palindrome):
                if is_palindrome(temp_string) == True:
                    longest_palindrome = temp_string
            j += 1
        #move forward one place, start over
        else:
            i += 1
            j = i+1

    return longest_palindrome


print "test 1: ", question2("racecar")
# test 1:  racecar
print "test 2: ", question2("cumquat") 
# test 2:  c
print "test 3: ",question2("forgeeksskeegfor and the the results")
# test 3:  geeksskeeg
print "test 4: ",question2("I love banana and racec r and cumquat and all the other thing in all I geekskeegfor")
#test 4:  geekskeeg 


'''Question 3
Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest possible
 total weight of edges. Your function should take in and
 return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

Vertices are represented as unique strings. 
The function definition should be question3(G)
'''

import  string
parent = dict()
rank = dict()
#function to make parent list such as 'A':'A', 'B':'B','C':'C' 
#and initialize rank(weight) with 0
def make_set(vertice):
    parent[vertice] = vertice  
    rank[vertice] = 0
#function to find set of element of vertice     
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
#         print "parent:",parent
    return parent[vertice]
#function to union of two  sets vertice1 and vertice2    
def union(vertice1, vertice2):
    root1 = find(vertice1) 
    root2 = find(vertice2)
    
    if root1 != root2:
        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[root1] > rank[root2]: 
            parent[root2] = root1        
        else:
            parent[root1] = root2
            # #If ranks are same, then make one as root and increment
            # its rank by one
            if rank[root1] == rank[root2]: rank[root2] += 1
                           
#kruskal algorithm to construct Minimum Spanning tree         
def question3(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    
    output_dict=dict()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        # If including this edge does't cause cycle, include it
        # in minimum_spanning_tree and store output_dit,dictionary with key of vertice1
        # and value,which has list structure with (vertice2,weight)
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
            output_dict[vertice1]=list((vertice2,weight))
#     output_dict = sorted(output_dict.items(), key=lambda s: s[0])
    return output_dict
             
#As for adjacent list, I use a dictionary, where the dictionary keys are the vertices, and the values are the weights.
testgraph1 = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',1)]} 
testgraph2 = {'A': [('B', 2)],'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}   
testgraph3 = {'A':[('B',7),('D',5)],'B':[('C',8),('D',9),('E',7)]}
testgraph4 = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',0)]}

#change testgraph1 to dictionary, such as graph1 = {'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
#         'edges': set([ (1, 'A', 'B'),(5, 'A', 'C'), (3, 'A', 'D'),(4, 'B', 'C'), (2, 'B', 'D'), (1, 'C', 'D'),
#           ])}
def make_edges_list(testgraph):
    graph_set=set()
    for k,v in testgraph.iteritems():  # number of key : 3
        i = 0 
        num_v=len(v) #number of value = key : 3, 2, 1
        num_k=len(v[0]) # value each element's length : 2, 2, 2
#       set() consist of (rank(weight), from_node, to_node)    
        for  i in xrange(num_v):
            for j in xrange(num_k):
                j=0
                graph_set.add((testgraph.get(k)[i][j+1],k,testgraph.get(k)[i][j]))                  
    key_list=list(string.ascii_uppercase[:len(graph_set)])    
    graph_dict={ 'vertices':key_list,'edges':graph_set,}    
    return graph_dict
 
graph1= make_edges_list(testgraph1)
graph2= make_edges_list(testgraph2)
graph3= make_edges_list(testgraph3)
graph4= make_edges_list(testgraph4)  
  
print question3(graph1)
#{'A': ['B', 1], 'C': ['D', 1], 'B': ['D', 2]}
print question3(graph2)
#{'A': ['B', 2], 'B': ['C', 5]}
print question3(graph3)
#{'A': ['B', 7], 'B': ['C', 8]}
print question3(graph4)
#{'A': ['B', 1], 'C': ['D', 0], 'B': ['D', 2]}


''' Question 4:
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

def question4(T, root, n1, n2):
    if n1<root and root <= n2:  #check whether it is balanced tree, if so, root is common ancestor of n1,n2
        return root
    else : #otherwise(unbalanced), left traversal
        for i in xrange(len(T)): #It is binary search tree,where left child < root <= right child.    
            if T[root][i] == 1: #Find only first element of  which element is 1, is left child and  it become new root and stop for  loop.                 
                root= i              
                break       
        return question4(T, root, n1, n2)       


print "test 1:",question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
# test 1: 3
print "test 2:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,2,5)
# test 2: 3
print "test 3:",question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,1,0]],3,0,2)
# test 3: 1



"""
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 
5 elements, the 3rd element from the end is the 3rd element. The function definition should look like 
"question5(ll, m)", where ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node in the linked list. Return 
the value of the node at that position.
"""

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:  #if head is exist(not None)
            while current.next:   #and if current's next element exist
                current = current.next     #shift to next 
            current.next = new_element   #current's next element become new_element.   
        else:
            self.head = new_element
            
#calculate the  size of linked  list    
    def linked_list_size(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count

# Assume the first position is 1.
# Return "None" if position is not in the list.
    def question5(self,ll,m):    
        counter = 1
        ll = self.head
        l_size = self.linked_list_size()
#         print "linked list size:", l_size
        if m < 1:   # None for the first position less than  0
            return None
        # m is the "mth number from the end, which is  equal element with (linked_list size+1)-m from start.
        while ll :  #while current exit(not None)
            if counter == (l_size+1)-m:                    
                return ll.data
            ll = ll.next
            counter += 1
        return None


print "test set 1 :"
#create Node with 1,2,3,4,5    
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
#Find value for each element of position from end: 1,2,3,4,5
print ll.question5(ll, 1)
print ll.question5(ll, 2)
print ll.question5(ll, 3)
print ll.question5(ll, 4)
print ll.question5(ll, 5)
# test set 1 :
# 5
# 4
# 3
# 2
# 1

    
print "test set 2 :"
#create Node with 1,2,3,4,5,6    
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)
# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)
#Find value for each element of position from end: 1,2,3,4,5
print ll.question5(ll, 1)
print ll.question5(ll, 2)
print ll.question5(ll, 3)
print ll.question5(ll, 4)
print ll.question5(ll, 5)
print ll.question5(ll, 6)
# test set 2 :
# 6
# 5
# 4
# 3
# 2
# 1


print "test set 3 :"
#create Node with 6,5,4,0, ,3   
e1 = Node(6)
e2 = Node(5)
e3 = Node(4)
e4 = Node(0)
e5 = Node('')
e6 = Node(3)
# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)
#Find value for each element of position from end: 1,2,3,4,5
print ll.question5(ll, 1)
print ll.question5(ll, 2)
print ll.question5(ll, 3)
print ll.question5(ll, 4)
print ll.question5(ll, 5)
print ll.question5(ll, 6)
# test set 3 :
# 3
# 
# 0
# 4
# 5
# 6
    



