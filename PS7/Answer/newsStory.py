class NewsStory(object):
    ''' Implements a newsfeed object '''
    
    def __init__(self, gid, tit, subj, summ, lnk):
        self.gid = gid
        self.tit = tit
        self.subj = subj
        self.summ = summ
        self.lnk = lnk
        
    def getGuid(self):
        return self.gid
        
    def getTitle(self):
        return self.tit
        
    def getSubject(self):
        return self.subj

    def getSummary(self):
        return self.summ
        
    def getLink(self):
        return self.lnk
        
# end of code for class newsStory