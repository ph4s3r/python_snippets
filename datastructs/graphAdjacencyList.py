
# Whole graph in a dict
graph = dict()

# Nodes are dict keys

# Outbound edges to other nodes are stored as values in a list format

graph['A'] = ['B', 'C']
graph['B'] = ['E' ,'C', 'A']
graph['C'] = ['A', 'B', 'E' ,'F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']

