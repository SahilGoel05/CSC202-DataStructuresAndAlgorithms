from stack_array import *

class vertex:
    def __init__(self, adjacencies: List):
        self.in_degree = 0
        self.adjacencies = adjacencies

def tsort(vertices: List) -> str:
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    elif len(vertices) % 2 == 1:
        raise ValueError("input contains an odd number of tokens")

    graph: List = []
    for i in range(len(vertices)):
        add = True
        for j in range(len(graph)):
            if vertices[i] == graph[j][0]:
                add = False
        if add:
            graph.append((vertices[i], vertex([])))

    for i in range(0, len(vertices), 2):
        start = vertices[i]
        end = vertices[i + 1]
        for j in range(len(graph)):
            if start == graph[j][0]:
                graph[j][1].adjacencies.append(end)
        for j in range(len(graph)):
            if end == graph[j][0]:
                graph[j][1].in_degree += 1

    for i in range(len(graph)):
        for j in range(len(graph[i][1].adjacencies)):
            for k in range(len(graph)):
                if graph[i][1].adjacencies[j] == graph[k][0]:
                    for l in range(len(graph[k][1].adjacencies)):
                        if graph[k][1].adjacencies[l] == graph[i][0]:
                            raise ValueError("input contains a cycle")


    output_string = ""
    node_stack = Stack(len(graph))
    node_stack.push("TEMPREMOVETHISNOW")
    while (not node_stack.is_empty()) or len(graph) > 0:
        if (not node_stack.is_empty()) and node_stack.peek() == "TEMPREMOVETHISNOW":
            node_stack.pop()
        remove_adjacencies = -1
        for i in range(len(graph)):
            if graph[i][1].in_degree == 0:
                remove_adjacencies = i
        node_stack.push(graph[remove_adjacencies][0])
        for j in range(len(graph[remove_adjacencies][1].adjacencies)):
            for k in range(len(graph)):
                if graph[remove_adjacencies][1].adjacencies[j] == graph[k][0]:
                    graph[k][1].in_degree -= 1
        graph.pop(remove_adjacencies)
        if not node_stack.is_empty():
            output_string += node_stack.pop() + "\n"

    return output_string
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
