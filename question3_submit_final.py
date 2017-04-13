
import  string
import collections
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
    output_dict=dict()
#     print "after list(graph['edges']) sort:",edges
    for edge in edges:
        weight, vertice1, vertice2 = edge
        print "&&&",weight, vertice1, vertice2, edge
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
            output_dict[vertice1]=list((vertice2,weight))
#     print "%%% output_dict:",output_dict
#     return minimum_spanning_tree
#     ordered_output_dict=collections.OrderedDict(sorted(output_dict.keys())) #( , ) result
#     output_dict=output_dict.keys().sort(key = lambda s: s[0])  #error since dict.keys():error,shd be .items()
    sorted_dict = sorted(output_dict.items(), key=lambda s: s[0])
#     sorted_dict = sorted(output_dict.items(), key=lambda (key, val): key[0]) #same  as  above
#     sorted_dict= dict(sorted_dict)
#     return sorted_dict
    return output_dict
    


             
#my add
testgraph = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',1)]}    
###
graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }
minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])

def make_edges_list(testgraph):
    graph_set=set()
    key_list=[]
     
    for k,v in testgraph.iteritems():  # number of key : 3
        i = 0 
#         j = 0  # j 0,1 then 1 ,2 ->  out of index error
        num_v=len(v) #number of value = key : 3, 2, 1
        num_k=len(v[0]) # value each element's length : 2, 2, 2
        print "num_v, num_k:",num_v, num_k
#         key_list.append(k)  #not correct,which is not[ 'A','C','B'] but  [ABCDEF]
#       set() consist of (rank(weight), from_node, to_node)  
        
        for  i in xrange(num_v):
            for j in xrange(num_k):
                j=0
                graph_set.add((testgraph.get(k)[i][j+1],k,testgraph.get(k)[i][j]))
                
                         
#                 print "i,j,j+1:",i,j,j+1      
    print "*-*len(graph_set)",len(graph_set)  
    key_list=list(string.ascii_uppercase[:len(graph_set)])    
    graph_dict={ 'vertices':key_list,'edges':graph_set,}    
    return graph_dict
 
# print "$$$ make_edges_list(testgraph): \n",make_edges_list(testgraph)
# graph= make_edges_list(testgraph)
# print "******graph",graph
# assert kruskal(graph) == minimum_spanning_tree
print "#######found result is : ",kruskal(graph)
print
# set([(1, 'A', 'B'), (1, 'C', 'D'), (2, 'B', 'D')])
# should be : {'A':[('B',1)], 'B':[('D',2)], 'C':['D':1)]}
print "list(graph['edges']):",list(graph['edges'])


## even I changed  to use original graph,  which made  from such as graph = {
#         'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
#         'edges': set([..} the result is same  with input format of  dictiorany from udacity 
#
