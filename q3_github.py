"""
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects 
all vertices in a graph with the smallest possible total weight of edges. Your function should take in 
and return an adjacency list structured like this: {'A':[('B',2)],'B':[('A',2),('C',5)],'C':[('B',5)]}. 
Vertices are represented as unique strings. The function definition should be "question3(G)"
"""


"""
T = {}
min_dist = float('inf')
for vertex in G:
    T[vertex] = []
    #sort edges in G in ascending order
    for edge in G[vertex]:
        if edge[0] not in T:
            if edge[1] < min_dist:
                mintuple = (edge[0], edge[1])
                min_dist = edge[1]
        else:
            mintree[vertex].append((edge[0], edge[1]))
"""
parent = dict()
rank = dict()

def question3(G):
    vertices = G.keys()
    print "vertices:",vertices  #'A','B','C'
    p = {}   #parent node #parent
    r = {}   #rank 
    for vertice in vertices:
        p[vertice] = vertice
        r[vertice] = 0  
    print "p  parent  dictionary with  same  key:value :",p    
    min_spanning_tree = []
    edges = []
    for node in vertices:
        edges.sort()
        print "node, edges:",node, edges
        
#     edges= list(testgraph)    
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
                union(vertice1, vertice2)
                min_spanning_tree.add(edge)
    return min_spanning_tree

    
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]
    
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1
    
# testgraph = {'A':[('B',2)],'B':[('A',2),('C',5)],'C':[('B',5)]}
testgraph = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',1)]}
print question3(testgraph)
#{
