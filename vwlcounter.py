# vowel counter
# vwlcounter.py

counter = 0; # counter

# following line must be eliminated before submitting to grader
s = raw_input('Vowel counter. Please enter string to count. ');

# main loop
for char in s:
    if char == 'a':
        counter += 1;
    elif char == 'e':
        counter += 1;
    elif char == 'i':
        counter += 1;
    elif char == 'o':
        counter += 1;
    elif char == 'u':
        counter += 1;
print('Number of vowels: ' + str(counter));
# end of code    