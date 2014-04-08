# Guessing the secret number
# guessing.py

low = 0; high = 100;     # bisect search limits
sn = 0;                 # secret number

# Introduction
print('Please think of a number between 0 and 100!'); # Introduce the game 

# first guess
sn += round(int((high - low)/2));

# Main Loop
while True:
    print('Is your secret number ' + str(int(sn))+ '?'); # get feedback
    reply = raw_input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter"c" to indicate I guessed correctly. '); # get feedback
    if reply == 'l': # guess too low; 
        low = sn; # make guess new lower limit
        if low == high: # just in case the bastard is giving me a hard time
            break;       
        sn = low + int((high - low)/2); # and calculate new guess   
    elif reply == 'h': # guess too high; 
        high = sn; # make guess new highest limit
        if low == high: # just in case the bastard is giving me a hard time
            break;
        sn = low + int((high - low)/2); # and calculate new guess
    elif reply == 'c': # hit it!
        break; # get out of loop 
    else:
        print('Sorry. I did not understand your input.'); # the user entered something else
        
# Ending        
print('Game over. Your secret number was: ' + str(int(sn)));
