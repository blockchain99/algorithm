
class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []  #list
        self.edges = edges or []  #list
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)
    def get_node_names(self):
        return self.node_names
    
graph = Graph()
graph.set_node_names(('Mountain View',   # 0
                      'San Francisco',   # 1
                      'London',          # 2
                      'Shanghai',        # 3
                      'Berlin',          # 4
                      'Sao Paolo',       # 5
                      'Bangalore')) 
print graph.get_node_names()

test_list = list(('Mountain View',   # 0
                      'San Francisco',   # 1
                      'London',          # 2
                      'Shanghai',        # 3
                      'Berlin',          # 4
                      'Sao Paolo',       # 5
                      'Bangalore'))
print "test_list : ",test_list
print "test_list[0]:",test_list[0]


# test_list2 = list('Mountain View',   # 0   #TypeError: list() takes at most 1 argument (7 given)
#                       'San Francisco',   # 1
#                       'London',          # 2
#                       'Shanghai',        # 3
#                       'Berlin',          # 4
#                       'Sao Paolo',       # 5
#                       'Bangalore')
# print "test_list2 : ",test_list2  #TypeError: list() takes at most 1 argument (7 given)