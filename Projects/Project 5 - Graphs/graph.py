from typing import Any, List, Optional
from stack_array import * # Needed for Depth First Search
from queue_array import * # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key: Any):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to: List = []


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename: str):
        self.vertices: List = []

        try:
            temp_read_file = open(filename, "r")
        except FileNotFoundError:
            raise FileNotFoundError("File can not be found")

        while self.has_line(temp_read_file):
            line = temp_read_file.readline().strip("\n")

            space_index = line.find(" ")
            vertex_1 = line[0: space_index]
            vertex_2 = line[space_index + 1: len(line)]

            self.add_vertex(vertex_1)
            self.add_vertex(vertex_2)
            self.add_edge(vertex_1, vertex_2)

        temp_read_file.close()

        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''

    def has_line(self, file: Any) -> bool:
        pos = file.tell()
        ret = bool(file.readline())
        file.seek(pos)
        return ret

    def add_vertex(self, key: Any) -> None:
        skip = False
        for i in range(len(self.vertices)):
            if self.vertices[i].id == key:
                skip = True
        if not skip:
            self.vertices.append(Vertex(key))
        '''Add vertex to graph, only if the vertex is not already in the graph.'''

    def get_vertex(self, key: Any) -> Optional[Vertex]:
        for i in range(len(self.vertices)):
            if self.vertices[i].id == key:
                return self.vertices[i]
        return None
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''

    def add_edge(self, v1: Any, v2: Any) -> None:
        vertex_1 = self.get_vertex(v1)
        vertex_2 = self.get_vertex(v2)
        vertex_1.adjacent_to.append(v2)
        vertex_2.adjacent_to.append(v1)
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''

    def get_vertices(self) -> List:
        return self.vertices.sort()
        '''Returns a list of id's representing the vertices in the graph, in ascending order
           Note: Results of Python sort on the list satisifies ascending order requirement'''

    def conn_components(self) -> List:
        visited = [False] * len(self.vertices)
        final_connections = []

        for cur in range(len(self.vertices)):
            if not visited[cur]:
                iterative_connections = []
                final_connections.append(self.depth_first_search(iterative_connections, cur, visited))

        for i in range(len(final_connections)):
            for j in range(len(final_connections[i])):
                final_connections[i][j] = self.vertices[final_connections[i][j]].id

        for i in range(len(final_connections)):
            final_connections[i].sort()

        return final_connections
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list should contain the 
           vertices (in 'Python List Sort' order) in the connected component represented by that list.
           The overall list of lists should also be in order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''

    def depth_first_search(self, iterative_connections, cur, visited):
        visited[cur] = True
        iterative_connections.append(cur)

        for i in range(len(self.vertices[cur].adjacent_to)):
            actual_index = -1
            for j in range(len(self.vertices)):
                if self.vertices[j].id == self.vertices[cur].adjacent_to[i]:
                    actual_index = j
            if not visited[actual_index]:
                iterative_connections = self.depth_first_search(iterative_connections, actual_index, visited)

        return iterative_connections

    def is_bipartite(self) -> bool:
        all_subgraphs = self.conn_components()
        for i in range(len(all_subgraphs)):
            for j in range(len(all_subgraphs[i])):
                for k in range(len(self.vertices)):
                    if self.vertices[k].id == all_subgraphs[i][j]:
                        all_subgraphs[i][j] = self.vertices[k]

        for z in range(len(all_subgraphs)):
            colors_array = [-1] * len(all_subgraphs[z])
            colors_array[0] = 1
            q = Queue(len(all_subgraphs[z]))
            q.enqueue(0)

            while not q.is_empty():
                u = q.dequeue()

                for v in range(len(all_subgraphs[z][u].adjacent_to)):
                    actual_index = -1
                    for k in range(len(all_subgraphs[z])):
                        if all_subgraphs[z][k].id == all_subgraphs[z][u].adjacent_to[v]:
                            actual_index = k

                    if colors_array[actual_index] == -1:
                        colors_array[actual_index] = 1 - colors_array[u]
                        q.enqueue(actual_index)
                    elif colors_array[actual_index] == colors_array[u]:
                        return False

        return True
        '''Returns True if the graph is bicolorable and False otherwise.
        This method MUST use Breadth First Search logic!'''
