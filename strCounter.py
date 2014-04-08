# string counter
# str counter

counter = 0; # counter
i = 0; # string index

# following lines must be removed before submitting to grader
s = raw_input('Enter string to scan. ');
t = raw_input('Enter string to count. ');

# following line must be uncommented before submitting to grader
# t = 'bob';

# main loop
while i <= len(s) - len(t):
    if s[i:i+len(t):1] == t:
        counter += 1;
    i += 1;
print ('Number of times ' + t + ' occurs is: ' + str(counter));
# end of code