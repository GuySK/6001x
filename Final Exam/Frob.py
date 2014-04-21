# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if newFrob.myName() >= atMe.myName(): 
        if atMe.getAfter() == None:                 # I have no next node
            atMe.setAfter(newFrob)             
            newFrob.setBefore(atMe)             
            return
        else:                                       # check if it belongs here 
            if newFrob.myName() <= atMe.getAfter().myName():
                # insert Frob
                newFrob.setAfter(atMe.getAfter()) # After link passed to new node
                newFrob.setBefore(atMe)           # Before link must point to me
                atMe.getAfter().setBefore(newFrob) # Before link in next node must point to new Frob
                atMe.setAfter(newFrob)            # set my after link to new frob
            else:
                # pass the ojb to the next node
                return insert(atMe.getAfter(), newFrob)
    else: 
        if atMe.getBefore() == None:                # no one before me
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
            return
        else:
            return insert(atMe.getBefore(), newFrob)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore() == None:
        return start
    else:
        return findFront(start.getBefore())    

# testing

mark = Frob('mark')
craig = Frob('craig')
jayne = Frob('jayne')
martha = Frob('martha')
nick = Frob('nick')
sam = Frob('sam')
xanthi = Frob('xanthi')

insert(sam,nick)
insert(nick, xanthi)
insert(nick,martha)
insert(martha, jayne)
