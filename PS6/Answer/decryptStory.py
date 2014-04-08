from ps6_encryption import *

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
    
# end of code for decryptStory