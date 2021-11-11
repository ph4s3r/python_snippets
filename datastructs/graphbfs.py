
from collections import deque

# the graph is represented with an adjacency list, which is technically a dict
graph_AL = dict()

# Nodes are dict keys
# Outbound edges to other nodes are stored as values in a list format

# graph_AL['A'] = ['B', 'C']
# graph_AL['B'] = ['E', 'C', 'A']
# graph_AL['C'] = ['A', 'B', 'E', 'F']
# graph_AL['E'] = ['B', 'C']
# graph_AL['F'] = ['C']


graph_AL['A'] = ['B', 'C']
graph_AL['B'] = ['E', 'C', 'A']
graph_AL['C'] = ['A', 'B', 'E', 'F']
graph_AL['E'] = ['B', 'C', 'F']
graph_AL['F'] = ['C', 'G', 'E', 'H', 'I']
graph_AL['I'] = ['F', 'J']
graph_AL['G'] = ['L', 'K']
graph_AL['L'] = ['K']
graph_AL['K'] = ['L']



def bfs_q(input_graph: dict, start_node, end_node) -> deque:

    """
    BFS shortest path finder
    Usage e.g. print(bfs_q(graph_AL, 'A', 'F'))
    This bfs search is designed to work only with the above adjacency list / dict
    Works with graphs with loops and bidirectional edges
    """

    def node_in_q(d: deque, t: str) -> bool:
        for elem in d:
            if t in elem:
                return True
        return False


    q = deque()

    # q.popleft pops the leftmost element

    q.append(start_node) # q.append puts an element to the rightmost place
    adder = ""

    while not node_in_q(q, end_node): # stop when we reached the end node
        adder = q.popleft() # remove the leftmost element, to add paths to it to then reinsert on the right
        for conn in input_graph[adder[-1][-1]]: # trying all paths from here: e.g. having a path in adder var of 'ABC',
            # getting adder[0][-1] which is 'C', where input_graph['C'] will return all possible routes from C
            newpath = adder + conn
            if not node_in_q(q, conn): # making sure we don`t have a path through / to this node already
                q.append(newpath)

    return q.pop()


print(bfs_q(graph_AL, 'A', 'L'))


