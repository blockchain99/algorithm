import  string
# parent = dict()
# rank = dict()
# #function to make parent list such as 'A':'A', 'B':'B','C':'C' 
# #and initialize rank(weight) with 0
# def make_set(vertice):
#     parent[vertice] = vertice  
#     rank[vertice] = 0
# #function to find set of element of vertice     
# def find(vertice):
#     if parent[vertice] != vertice:
#         parent[vertice] = find(parent[vertice])
# #         print "parent:",parent
#     return parent[vertice]
# #function to union of two  sets vertice1 and vertice2    
# def union(vertice1, vertice2):
#     root1 = find(vertice1) 
#     root2 = find(vertice2)
#     
#     if root1 != root2:
#         # Attach smaller rank tree under root of high rank tree
#         # (Union by Rank)
#         if rank[root1] > rank[root2]: 
#             parent[root2] = root1        
#         else:
#             parent[root1] = root2
#             # #If ranks are same, then make one as root and increment
#             # its rank by one
#             if rank[root1] == rank[root2]: rank[root2] += 1
#                
#             
# #kruskal algorithm to construct Minimum Spanning tree         
# def question3(graph):
#     for vertice in graph['vertices']:
#         make_set(vertice)
#     
#     minimum_spanning_tree = set()
#     edges = list(graph['edges'])
#     edges.sort()
#     
#     output_dict=dict()
#     for edge in edges:
#         weight, vertice1, vertice2 = edge
#         # If including this edge does't cause cycle, include it
#         # in minimum_spanning_tree and store output_dit,dictionary with key of vertice1
#         # and value,which has list structure with (vertice2,weight)
#         if find(vertice1) != find(vertice2):
#             union(vertice1, vertice2)
#             minimum_spanning_tree.add(edge)
#             output_dict[vertice1]=list((vertice2,weight))
# #     output_dict = sorted(output_dict.items(), key=lambda s: s[0])
# 
#     return output_dict
#              
# #As for adjacent list, I use a dictionary, where the dictionary keys are the vertices, and the values are the weights.
# testgraph1 = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',1)]} 
# testgraph2 = {'A': [('B', 2)],'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}   
# testgraph3 = {'A':[('B',7),('D',5)],'B':[('C',8),('D',9),('E',7)]}
# testgraph4 = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',0)]}
# testgraph5 = {'A':[('B',10),('C',6),('D',5)],'B':[('D',15)],'C':[('D',4)]}
# 
# #change testgraph1 to dictionary, i.e. graph1 = {'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
# #         'edges': set([ (1, 'A', 'B'),(5, 'A', 'C'), (3, 'A', 'D'),(4, 'B', 'C'), (2, 'B', 'D'), (1, 'C', 'D'),
# #           ])}
# def make_edges_list(testgraph):
#     graph_set=set()
# 
#      
#     for k,v in testgraph.iteritems():  # number of key : 3
#         i = 0 
# 
#         num_v=len(v) #number of value = key : 3, 2, 1
#         num_k=len(v[0]) # value each element's length : 2, 2, 2
# 
# #       set() consist of (rank(weight), from_node, to_node)    
#         for  i in xrange(num_v):
#             for j in xrange(num_k):
#                 j=0
#                 graph_set.add((testgraph.get(k)[i][j+1],k,testgraph.get(k)[i][j]))
#                     
#     key_list=list(string.ascii_uppercase[:len(graph_set)])    
#     graph_dict={ 'vertices':key_list,'edges':graph_set,}    
#     return graph_dict
#  
# graph1= make_edges_list(testgraph1)
# graph2= make_edges_list(testgraph2)
# graph3= make_edges_list(testgraph3)
# graph4= make_edges_list(testgraph4)  
# graph5= make_edges_list(testgraph5)  
# print question3(graph1)
# #{'A': ['B', 1], 'C': ['D', 1], 'B': ['D', 2]}
# print question3(graph2)
# #{'A': ['B', 2], 'B': ['C', 5]}
# print question3(graph3)
# #{'A': ['B', 7], 'B': ['C', 8]}
# print question3(graph4)
# #{'A': ['B', 1], 'C': ['D', 0], 'B': ['D', 2]}
# print question3(graph5)

##################################################################
# Python program for Kruskal's algorithm to find Minimum Spanning Tree
# of a given connected, undirected and weighted graph
 
from collections import defaultdict
 
#Class to represent a graph
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary to store graph
         
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
        
#change testgraph1 to dictionary, i.e. graph1 = {'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
#         'edges': set([ (1, 'A', 'B'),(5, 'A', 'C'), (3, 'A', 'D'),(4, 'B', 'C'), (2, 'B', 'D'), (1, 'C', 'D'),
#           ])}        
    def make_edges_list(self,testgraph):
        self.graph_set=set()
     
        for k,v in testgraph.iteritems():  # number of key : 3
            i = 0 

            num_v=len(v) #number of value = key : 3, 2, 1
            num_k=len(v[0]) # value each element's length : 2, 2, 2

#           set() consist of (rank(weight), from_node, to_node)    
            for  i in xrange(num_v):
                for j in xrange(num_k):
                    j=0
#                     self.graph_set.add((testgraph.get(k)[i][j+1],k,testgraph.get(k)[i][j]))
                    self.graph.append([testgraph.get(k)[i][j+1],k,testgraph.get(k)[i][j]])
        key_list=list(string.ascii_uppercase[:len(self.graph_set)])    
        graph_dict={ 'vertices':key_list,'edges':self.graph_set,}    
        return graph_dict
 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        #If ranks are same, then make one as root and increment
        # its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's algorithm
    def KruskalMST(self):
 
        result =[] #This will store the resultant MST
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]
 
        #Step 1:  Sort all the edges in non-decreasing order of their
        # weight.  If we are not allowed to change the given graph, we
        # can create a copy of graph
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        #print self.graph
 
        parent = [] ; rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
     
        # Number of edges to be taken is equal to V-1
        while e < self.V -1 :
 
            # Step 2: Pick the smallest edge and increment the index
            # for next iteration
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
 
            # If including this edge does't cause cycle, include it
            # in result and increment the index of result for next edge
            if x != y:
                e = e + 1  
                result.append([u,v,w])
                self.union(parent, rank, x, y)          
            # Else discard the edge
 
        # print the contents of result[] to display the built MST
        print "Following are the edges in the constructed MST"
        for u,v,weight  in result:
            #print str(u) + " -- " + str(v) + " == " + str(weight)
            print ("%d -- %d == %d" % (u,v,weight))
 
 
# g = Graph(4)
# g.addEdge(0, 1, 10)
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)

#As for adjacent list, I use a dictionary, where the dictionary keys are the vertices, and the values are the weights.
testgraph1 = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',1)]} 
testgraph2 = {'A': [('B', 2)],'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}   
testgraph3 = {'A':[('B',7),('D',5)],'B':[('C',8),('D',9),('E',7)]}
testgraph4 = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',0)]}
testgraph5 = {'A':[('B',10),('C',6),('D',5)],'B':[('D',15)],'C':[('D',4)]}
 
g1=Graph(5) 
g1.make_edges_list(testgraph1)
g1.KruskalMST()
 
#This code is contributed by Neelam Yadav

