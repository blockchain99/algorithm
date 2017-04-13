'''
Created on Dec 6, 2016

@author: ys
'''

import collections
testgraph = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',1)]}    
###
# graph_dict=dict()
key_dict=dict()
val_dict=dict()
graph_tuple=()
key_list=[]
graph_set=set()
for k,v in testgraph.iteritems():
    print k,v
    print "len(v)",len(v) #3
    print "len(v[0]):",len(v[0]) #2
    print "v[0][0]",v[0][0] #B
    print "v[0][1]",v[0][1] #1
#     print sorted(v)
    key_list.append(k)
#     val_dict['edges']=(v,k)


#     for i in  xrange(len(v)):
#         for j in  xrange(len(v[0])):
#             graph_tuple += (v[i][j],)

#             new_tuple = (str(wid),) + (weight1,)  #( x, y)

    print "testgraph.get(k)[0]:",testgraph.get(k)[0][1]
    print (testgraph.get(k)[0][1],k,testgraph.get(k)[0][0]) #(4, 'B', 'C')
    print"-"*30
    graph_set.add((testgraph.get(k)[0][1],k,testgraph.get(k)[0][0]))

print "*"*20
print key_list    
print graph_set   
graph_dict={ 'vertices':key_list,'edges':graph_set,}
print graph_dict
print "*"*20

import string
testgraph = {'A':[('B',1),('C',5),('D',3)],'B':[('C',4),('D',2)],'C':[('D',1)]}  
    
for k,v in testgraph.iteritems():  # number of key : 3
        i = 0 
#         j = 0  # j 0,1 then 1 ,2 ->  out of index error
        num_v=len(v) #number of value = key : 3
        num_k=len(v[0]) # value each element's length : 2
        print "num_v, num_k:",num_v, num_k
        key_list.append(k)
#       set() consist of (rank(weight), from_node, to_node)  
       
        for  i in xrange(num_v):
            for j in xrange(num_k):
                j=0
#                 graph_set.add((testgraph.get(k)[i][j+1],string.ascii_uppercase[l],testgraph.get(k)[i][j]))
#                 print "i,j,j+1:",i,j,j+1 
                 

for  m in xrange(5):
    print string.ascii_uppercase[m]   
    
print "########## test#########"
q=0
for o in xrange(3):  
    for p in xrange(2):
        print string.ascii_uppercase[q]
    
        
       
        
            
         
                  
graph_dict={ 'vertices':key_list,'edges':graph_set,}  
 
print  graph_dict 
    
    


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

test_dict = {'A': ['B', 1], 'C': ['D', 1], 'B': ['D', 2]}

#test_dict = sorted(test_dict.items(), key=lambda s: s[0])
print test_dict

print dict(test_dict)
# print "sorted_dict:",sorted_dict











