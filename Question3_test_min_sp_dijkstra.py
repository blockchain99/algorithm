# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):  #vertex_obj.get_weight(neighbor_obj) - weight.
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
         return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
#         return str(self.id) + ' adjacent: ' + str(x.id for x in self.adjacent)
''''Graph, which holds the master list of vertices, and Vertex, 
which represents each vertex in the graph '''
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
     #my add   
    def get_edge(self):
        print self.vert_dict

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous
'''The shortest() function constructs the shortest path starting 
from the target ('e') using predecessors.'''
'''   
a = ('2',)
b = 'z'
new = a + (b,)
print new   #result : ('2', 'z')
'''   
total_my_dict=dict()
def shortest(v, path):  #vertex.  path
    ''' make shortest path from v.previous'''
    list_output = []
    my_dict=dict()
    if v.previous:
        
        print "@@@ v.previous.get_id():",v.previous.get_id()
        path.append(v.previous.get_id())
        shortest(v.previous, path)
#         print"&& v.previous:", v.previous,"&& path:", path
        print"&& v.previous:", v.previous#,"&& path:", path
        print "--",v.previous.get_id()  #return a, c 
#         print dict_new[v.previous.get_id()]  #dict_new[a], shows [('f', 14), ('c', 9), ('b', 7)]       
#         list_output.append(dict_new[v.previous.get_id()])
#         my_dict[v.previous.get_id()]=list_output
       
        my_dict[v.previous.get_id()]=dict_new[v.previous.get_id()]
    print "***list_output:",list_output   
    print "++ my_dict",my_dict 
    total_my_dict.update(my_dict)
    return total_my_dict

import heapq
'''The function dijkstra() calculates the shortest path
Dijkstra's algorithm is an iterative algorithm that 
provides us with the shortest path from one particular starting node
 (a in our case) to all other nodes in the graph. 
 Again this is similar to the results of a breadth first search.
'''
def dijkstra(aGraph, start):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    
    
  #  print "***",g.get_edge().get_weight()  #error
    #test tuple    
    a1 = ('2',)
    b1 = 'z'
    new1 = a1 + (b1,)
    print new1  #('2', 'z')
    
    print 'Graph data:'
    dict_new = dict()
    for v in g:  #from vertex
        new_list1=[]
        for w in v.get_connections():  #to vertex
            vid = v.get_id()  #from vertex id
            wid = w.get_id()  #to vertex id
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))
            vid1=(str(wid),)
            weight1=v.get_weight(w) 
            new_tuple = vid1 + (weight1,)
            new_list1.append(new_tuple)
#         print str(vid),":",new_list1   
        dict_new[vid]=new_list1
    print "adjecent list:",dict_new       
    from_point = 'a'
    dijkstra(g, g.get_vertex(from_point))  #from  vertex
    for t in ['d','e','f']:         #to vertex
        target = g.get_vertex(t)    #target is each of to vertex
        path = [t]
        out = shortest(target, path)
#         print "*shortest(target, path):",shortest(target, path)
        print 'From vertex :%s to :%s shortest path : %s' %(from_point,t, path[::-1])
        print out

   
          
   