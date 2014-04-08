def isVowel(char):
    vowels = 'AaEeIiOoUu'
    i = 0    
    while i < len(vowels):
        if char == vowels[i]:
            return True
        else: i += 1
    return False