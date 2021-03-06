
from util import Queue, Stack

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('vertex not found')

def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        g.add_edge(pair[1], pair[0])

    q = Queue()

    q.enqueue([starting_node])
    max_path = 1
    earliest_an = -1 # if the node has no parent

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if (len(path) >= max_path and v < earliest_an) or (len(path) > max_path):
            earliest_an = v
            max_path = len(path)
        
        for neighbor in g.vertices[v]:
            new_path = list(path)
            new_path.append(neighbor)
            q.enqueue(new_path)

    return earliest_an


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestors, 1), "====> 10") #, 10
print(earliest_ancestor(ancestors, 2), "====> -1") #, -1)
print(earliest_ancestor(ancestors, 3), "====> 10") #, 10)
print(earliest_ancestor(ancestors, 4), "====> -1") #, -1)
print(earliest_ancestor(ancestors, 5), "====> 4") #, 4)
print(earliest_ancestor(ancestors, 6), "====> 10") #, 10)
print(earliest_ancestor(ancestors, 7), "====> 4") #, 4)
print(earliest_ancestor(ancestors, 8), "====> 4") #, 4)
print(earliest_ancestor(ancestors, 9), "====> 4") #, 4)
print(earliest_ancestor(ancestors, 10), "====> -1") #, -1)
print(earliest_ancestor(ancestors, 11), "====> -1") #, -1)