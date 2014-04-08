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