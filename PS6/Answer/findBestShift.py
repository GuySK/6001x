from ps6_encryption import isWord
from applyShift import *

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """

    def splitText(text, dic):
        ''' split a text into words based on chars not in dic ''' 
        wordList = []
        i, j = 0, 0  
        for char in text:
            j += 1
            if char not in dic:
                wordList.append(text[i:j-1])
                i = j
        if i != j:
            wordList.append(text[i:j])
        
        return wordList
    # end of code for splitText    

    splitted= []                                # a list of words
    validWords = [0 for x in range(26)]     #a list of word counters
    
    for i in range(1,25):                  # try decoding with complementary shift
        shift = 26-i                          # current shift 
        dic = buildCoder(shift)              # build dictionary
        decText = applyShift(text, shift)    # decrypt text  
        splitted = splitText(decText, dic)   # split it into words
        
        for word in splitted:               # check for validity
            if isWord(wordList, word):
                validWords[shift] += 1
#    print 'valid words: ', max(validWords)  # comment this line before grading
    return validWords.index(max(validWords)) # return shift with max valid words
# end of code for findBestShift
