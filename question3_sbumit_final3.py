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




