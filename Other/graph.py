# Testing graph
testGraph = {'a':[], 'b':['a','c'], 'c':['a'], 'd':['e'], 'e':['c','b'],'f':['e'],'g':['f','d']}
#
def getSrcNodes(graph, node):
    ''' 
    Returns a list containing the node's source nodes in graph.
    graph is a dict, node a string.
    '''
    if graph.get(node,0) == 0:
        print('Node ' + str(node) + ' not in Graph.')
    else:
        return graph[node]
#    
def dist(graph, n1, n2):
    '''
    Returns distance and path from node n1 to n2 in graph.
    '''
    distances = []
    nodes = []
    
    if n2 in getSrcNodes(graph, n1):
        return (1, n2+n1)
    else:
        for node in getSrcNodes(graph, n1):
            d, n = dist(graph, node, n2)
            distances.append(d)
            nodes.append(n)
    
    if len(distances) == 0:
        return 0
    else:
        n = nodes[distances.index(min(distances))]        
        return (1 + min(distances), n+n1)
#
