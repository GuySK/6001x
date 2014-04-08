class Queue(object):
    ''' Implements a Queue '''
    
    def __init__(self):
        ''' Inits queue '''
        self.list = []    # init empty list
        
    def insert(self, elem):
        ''' Inserts an element in the queue '''
        self.list.append(elem)
        
    def remove(self):
        ''' pops next element from queue '''
        try:
            return self.list.pop(0) # returns first element and removes it
        except:
            raise ValueError
    #end of remove method        