def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
#   print text
    if len(text) <= lineLength:
        return text
    else:
        space = False
        for i in range(len(text)-lineLength): 
            if text[lineLength +i] == ' ':
                space = True
                newL = lineLength + i
                break                
        if not space:
            return text + '\n'
        else: 
            return (text[:newL] + '\n' + insertNewlines(text[newL+1:], lineLength))
        
# end of code for insertNewlines