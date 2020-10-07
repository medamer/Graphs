from util import Queue, Stack

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
        graph.add_edge(pair[1], pair[0])
    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # If the path is longer or equal and the value is smaller, or if the path is longer)
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor


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