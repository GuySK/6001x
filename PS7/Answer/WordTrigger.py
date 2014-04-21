import string

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError
        
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
        
    def evaluate(self, story):
        return not self.trigger.evaluate(story)        
        
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        return (self.trigger1.evaluate(story) and self.trigger2.evaluate(story))        

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        return (self.trigger1.evaluate(story) or self.trigger2.evaluate(story))        

class WordTrigger(Trigger):
    ''' Implements a word trigger abstract class '''
    
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        ''' 
        Returns True if trigger's word in the string 'text'.
        '''
        specialChars = string.punctuation
        newtext = ''
        
        for i in range(len(text)): 
            if text[i] in specialChars:
                newtext += ' '
            else:
                newtext += text[i]
        
        listWords = string.split(newtext,' ')
        lowList = [w.lower() for w in listWords]
            
        if self.word in lowList:
            return True
        else:
            return False
                   
class TitleTrigger(WordTrigger):
    '''
    Implements a word trigger for stories' titles
    '''
        
    def evaluate(self, story):
        '''
        Evaluates if trigger word is present in the newsStory's title.
        '''
        if self.isWordIn(story.getTitle()):
            return True
        else:
            return False

class SubjectTrigger(WordTrigger):
    '''
    Implements a word trigger for stories' subjects
    '''
        
    def evaluate(self, story):
        '''
        Evaluates if trigger word is present in the newsStory's subject.
        '''
        if self.isWordIn(story.getSubject()):
            return True
        else:
            return False

class SummaryTrigger(WordTrigger):
    '''
    Implements a word trigger for stories' summaries
    '''
        
    def evaluate(self, story):
        '''
        Evaluates if trigger word is present in the newsStory's summary.
        '''
        if self.isWordIn(story.getSummary()):
            return True
        else:
            return False
            
class PhraseTrigger(Trigger):
    
    def __init__(self, phrase):
	    self.phrase = phrase
		
    def evaluate(self, story):
	if self.isPhraseIn(story):
           return True
        else:
            return False
		
    def isPhraseIn(self, story):
        if self.phrase in story.getTitle():
            return True
        elif self.phrase in story.getSubject():
            return True
        elif self.phrase in story.getSummary():
            return True
        else:
            return False

def filterStories(stories, triggerlist):
    ''' 
    Returns a list of stories that fire triggers in list
    stories: a list of stories. 
    ''' 
    filteredStories = []
    
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filteredStories.append(story)
                break
    return filteredStories
