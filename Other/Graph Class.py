# Implements Graph in OO mode
import string

class Graph(object):
    '''
    Implements a digraph.
    '''
    def __init__(self):
         self.nodes = {}

    def addNode(self, node):
        '''
        Adds a node to Graph
        '''
        node = string.upper(node)
        if self.nodes.get(node,0) != 0:
            raise ValueError('Node ' + str(node) + ' already in Graph')
        else:
            self.nodes[node] = []    # init node with empty list of edges

    def delNode(self, node):
        '''
        Removes a node from Graph
        '''
        node = string.upper(node)
        if node not in self.nodes:
            raise ValueError('Node ' + str(node) + ' not in Graph')
        else:
            for n in self.nodes:    # remove node from every other node's list
                if node in self.nodes[n]:
                    newNodeList = [x for x in self.nodes[n] if x != node]
                    self.nodes[n] = newNodeList
            del(self.nodes[node])    # and finally, remove node
   # end of delNode     

    def addEdge(self, node1, node2):
        '''
        Adds edge from node1 to node2
        '''        
        node1 = string.upper(node1)
        node2 = string.upper(node2)
        
        if self.nodes.get(node1,0) == 0:
            raise ValueError('Node ' + str(node1) + ' not in Graph')
        elif self.nodes.get(node2,0) == 0:
            raise ValueError('Node ' + str(node2) + ' not in Graph')
        else:
            if node1 in self.nodes[node2]:
                raise ValueError('Node ' + str(node1) + 'already in ' + str(node2) + '\'s list')
            else:
                self.nodes[node2].append(node1) # add edge from node1 to node2

                                
    def delEdge(self, node1, node2):
        '''
        Removes edge from node1 to node2    
        '''    
        node1 = string.upper(node1)
        node2 = string.upper(node2)

        if self.nodes.get(node1,0) == 0:
            raise ValueError('Node ' + str(node1) + ' not in Graph')
        elif self.nodes.get(node2,0) == 0:
            raise ValueError('Node ' + str(node2) + ' not in Graph')
        else:
            if node1 not in self.nodes[node2]:
                raise ValueError('Node ' + str(node1) + 'not in ' + str(node2) + '\'s list')
            else:
                self.nodes[node2].remove(node1) # removes edge from node1 to node2
                
                
    def getSrcNodes(self, node):
        ''' 
        Returns a list containing the node's source nodes in graph.
        '''
        node = string.upper(node)

        if self.nodes.get(node,0) == 0:
            raise ValueError('Node ' + str(node) + ' not in Graph.')
        else:
            return self.nodes[node]

          
    def getDistance(self, node1, node2):
        '''
        Returns distance from node n1 to n2
        '''
        node1 = string.upper(node1)
        node2 = string.upper(node2)
        distances = []    

        if node1 == node2:
            return 0
            
        if node2 in self.getSrcNodes(node1):
            return 1
        else:
            for node in self.getSrcNodes(node1):
                distances.append(self.getDistance(node, node2))

        if len(distances) == 0:
            return -1
        else:
            return 1 + min(distances)
    # end of getDistance
    
    def getPath(self, node1, node2):
        '''
        Returns path from node1 to node2
        '''
        node1 = string.upper(node1)
        node2 = string.upper(node2)
        paths = []    

        if node1 == node2:
            return node1
        
        if node2 in self.getSrcNodes(node1):
            return node2 + node1
        else:
            for node in self.getSrcNodes(node1):
                paths.append(self.getPath(node, node2))

        if len(paths) == 0:
            return 'XXX'    # dead end
        else:
            lengths = [len(x) for x in paths]
            shortestPath = paths[lengths.index(min(lengths))]
            return shortestPath + node1
        #end of getPath
            
def createGraph(lastNode):
    '''
    Used to test Class Graph. lastNode = greatest node to be created in graph.
    '''
    g = Graph()    # new graph
    nodeNames = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    edges = ['AB','AC','CB','BE','CE','BD','ED','CF','EF','DG','EG','FG','GH','FI','IH','IJ','HK','JK']
    numNodes = 1 + nodeNames.index(string.upper(lastNode))
    
    for node in nodeNames[:numNodes]:
        g.addNode(node)
        
    for edge in edges:
        if (edge[0] in g.nodes and edge[1] in g.nodes):
            g.addEdge(edge[0],edge[1])            
    return g                

# end of Class Graph    