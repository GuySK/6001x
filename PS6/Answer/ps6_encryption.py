# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "C:/Users/AAB330/6001x/PS6/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("C:/Users/AAB330/6001x/PS6/story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """

    lowcase = string.ascii_lowercase
    upcase =  string.ascii_uppercase
    codeDict = {}
    
    i = 0
    for letter in lowcase:
        codeDict[lowcase[i]] = lowcase[(i+shift)%26]
        i += 1
    
    i = 0
    for letter in upcase:
        codeDict[upcase[i]] = upcase[(i+shift)%26]
        i += 1        
    
    return codeDict    
# end of code for buildCoder    

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    cipherText = ''
    for char in text:
        cipherText += coder.get(char, char)
    return cipherText
# end of code for applyCoder

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))
# end of code for applyShift

# Problem 2: Decryption
#
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

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    
    wordList = loadWords()
    story = getStoryString()
    plainText = applyShift(story, findBestShift(wordList, story))
    return plainText
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
