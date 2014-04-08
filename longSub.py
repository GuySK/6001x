# Longest substring in alphabetical order detector
# longSub.py

counter = 0; # counter
i = 0; # substring index
j = 0; # string index
sub = ''; # substring
maxsub = ''; # longest substring 

# following line must be commented before submitting to grader
s = raw_input('Enter string to scan. ');

# check if string really present
while True: 
    if len(s) < 1: # no input provided
        break;
   
    sub = s[0]; # set up sub for the first time
    maxsub = sub; # just in case it is a one char string

# maint loop 
    while j+1 < len(s):
        while s[j+i+1] >= s[j+i]: # check if substring still in order
            sub += s[j+i+1] # if so add char to sub
#          print ('sub is: ' + sub); # debug sentence
            i += 1; # and move evaluation one char right
            if (j+i+1) == len(s): # string exhausted
                break; 
        if len(sub) > len(maxsub):
            maxsub = sub; # last sub detected is longest so far
#           print('maxsub is: ' + maxsub); # debug sentence
        j += 1; # move one position to the right in string
        sub = s[j]; # reset sub
        i = 0; # reset sub index
    break; # time to go home
# print('Longest substring in alphabeical order is: ' + maxsub + ' with length ' + str(len(maxsub))); # output result
print('Longest substring in alphabeical order is: ' + maxsub); # output result


# end of code