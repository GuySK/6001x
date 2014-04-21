class btNode(object):
    '''
    Implements a binary tree node
    '''
    def __init__(self, nodeid, value=None, parent=None):
        # node attributes
        self.id = None
        self.value = None
        self.parent = None
        self.children = []

        try:
            
            if parent == None:
                self.id = nodeid
                self.value = value
                return None
                
            if parent.insertChild(self) != None:
                self.id = nodeid
                self.parent = parent
                self.value = value
                return None
            else:
                raise Exception
        except:
            # abort object creation
            raise Exception('Error creating node')
            
    def setValue(self, value):
        self.value = value
    
    def getId(self):
        return self.id
        
    def getValue(self):
        return self.value
        
    def getParent(self):
        return self.parent
                
    def insertChild(self, node):
        
        if len(self.children) < 2:
            self.children.append(node)
            return len(self.children)
        return None
        
    def getChild(self, nchild=0):

        try:
            if nchild > 1:                # It's a binary tree my friend
                return None
            return self.children[nchild]
        except IndexError:              # Just in case child is not there
            return None
            
    def btSearch(self, val, stack):
        
    #    print("Node " + str(self.id) + " searching...")
    #    print("Stack contains "),
    #    for n in stack:
    #        print str(n.id),
    #    print " "
        
        if self.value == val:            # found it!
            return self                 

        stack.pop()                     # drops itself from the list          
        if len(self.children) == 0:     # No children. dead end.
            if len(stack) == 0:         # No nodes pending. Not found.
                return None
            else:
                nextNode = stack[-1]    # node to continue search
                return nextNode.btSearch(val, stack)
                
        for child in self.children[-1::-1]:   # get children into the stack
            stack.insert(len(stack), child)   # ... in the right order
            
        return self.getChild(0).btSearch(val, stack)    # continue searching
        
    def __str__(self):
        st =  'Id: ' +  self.id
        st += ', Value: ' + str(self.value)
        if self.parent != None:
            parent = self.parent.getId()
        else:
            parent = 'None'
        st += ', Parent: ' + parent
        if len(self.children) > 0:
            st += ', Leftchild: '+ self.children[0].getId()
        if len(self.children) > 1:
            st += ', Rightchild: '+ self.children[1].getId()
        return st        
        
def searchBT(node, value):
    '''
    Looks for a value in a binary tree. 
    node is the BT node where the search starts.
    Returns the node id that contains the value searched or None.
    '''
    stack = [node]  # init stack with first node
    return node.btSearch(value, stack) 
# end of code for searchBT

def mkBT(n, prefix='N', values=[], silent=True):
    '''
    Creates a binary tree of n nodes with the specified suffix.
    Optionally, a list of values may be passed through 'values'.
    ''' 
    # set up node names
    if prefix == None:
        prefix = 'N'
    
    # set up list of values for n values 
    if len(values) == 0:                # no list
        if not silent:
            print('Values will be initialized to 0')
        for i in range(n):
            values.append(0)
    else:        
        if n - len(values) < 0:         # list too long
            if not silent:
                print('Value list too long. Value list truncated to length '),
                print(str(n))
            newvalues = values[:n]
            values = newvalues
        elif n - len(values) > 0:      # list too short
            if not silent:
                print('Value list too short. Value list extended with value '),
                print(str(values[-1]))
            for i in range((n-len(values))):
                values.append(values[len(values)-1])
        else:                         # list is right length
            if not silent:
                print('Binary tree will be inizialized with list provided')                            
    
    # Create nodes
    nodeList = []
    nodeMap = []
    
    nodeId = prefix + str(0)            # Root node
    root = btNode(nodeId,values[0])       
    nodeList.append(root)
    nodeMap.append(root.getId())
    
    for i in range(0,n-1):              # Children nodes
        nodeId = prefix + str(i+1)
        if i%2 == 0:
            pindx = i/2
        node = btNode(nodeId,values[i+1],nodeList[pindx])
        nodeList.append(node)
        nodeMap.append(node.getId())
        if not silent:            
            print('Node ' + nodeId + ' created with parent ' + nodeMap[pindx]),
            print(' and value ' + str(values[i+1]))
        
    print('Binary Tree of ' + str(n) + ' nodes created successfully.')
    return root
# end of code for mkBT    
    