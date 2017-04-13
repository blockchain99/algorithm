parent = dict()
rank = dict()
    
def make_set(vertice):
    parent[vertice] = vertice  #'A':'A', 'B':'B','C':'C'
    rank[vertice] = 0
    
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
#         print "parent:",parent
    return parent[vertice]
    
def union(vertice1, vertice2):
    root1 = find(vertice1) 
    root2 = find(vertice2)
    
    print "@@ root1=from node :",root1,", root2=to node :",root2
    print "@@ rank[root1]", rank[root1],", rank[root2]",rank[root2]
    if root1 != root2:
        if rank[root1] > rank[root2]: #if weight of root1 bigger than weight of root2
            parent[root2] = root1     
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1
            print "## updated rank[root2] since rank[root2]=rank[root1]:",rank[root2]
    print  "^ parent:",parent
def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    
    print "after list(graph['edges']) sort:",edges
    for edge in edges:
        weight, vertice1, vertice2 = edge
        print "**",weight, vertice1, vertice2, edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
#         ####### my add
#         for verice_my in g:      
#             new_list1=[]
#             for  w in to_vertex :
#                 new_tuple = (str(wid),) + (weight1,)
#                 new_list1.append(new_tuple)
#             dict_new.append(new_list1)     
#         #######
    return minimum_spanning_tree

#my add
testgraph = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',1)]}    
###
# graph = {
#         'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
#         'edges': set([
#             (1, 'A', 'B'),
#             (5, 'A', 'C'),
#             (3, 'A', 'D'),
#             (4, 'B', 'C'),
#             (2, 'B', 'D'),
#             (1, 'C', 'D'),
#             ])
#         }

graph = {
        'vertices': ['A', 'B', 'C', 'D'],
        'edges': set([
            (2, 'A', 'B'),
            (2, 'B', 'A'),
            (5, 'B', 'C'),
            (5, 'C', 'B'),
            ])
        }

minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])

# assert kruskal(graph) == minimum_spanning_tree
print kruskal(graph)
# set([(1, 'A', 'B'), (1, 'C', 'D'), (2, 'B', 'D')])
# should be : {'A':[('B',1)], 'B':[('D',2)], 'C':['D':1)]}
print "list(graph['edges']):",list(graph['edges'])
