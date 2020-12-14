def string_letter_error(produced_string, correct_string):
    min_string_length = min(len(produced_string), len(correct_string))

    off = 0 

    off += abs(correct_string.count('a')-produced_string.count('a'))
    off += abs(correct_string.count('b')-produced_string.count('b'))
    off += abs(correct_string.count('c')-produced_string.count('c'))
    off += abs(correct_string.count('d')-produced_string.count('d'))
    off += abs(correct_string.count('e')-produced_string.count('e'))
    off += abs(correct_string.count('f')-produced_string.count('f'))
    off += abs(correct_string.count('g')-produced_string.count('g'))
    off += abs(correct_string.count('h')-produced_string.count('h'))
    off += abs(correct_string.count('i')-produced_string.count('i'))
    off += abs(correct_string.count('j')-produced_string.count('j'))
    off += abs(correct_string.count('k')-produced_string.count('k'))
    off += abs(correct_string.count('l')-produced_string.count('l'))
    off += abs(correct_string.count('m')-produced_string.count('m'))
    off += abs(correct_string.count('n')-produced_string.count('n'))
    off += abs(correct_string.count('o')-produced_string.count('o'))
    off += abs(correct_string.count('p')-produced_string.count('p'))
    off += abs(correct_string.count('q')-produced_string.count('q'))
    off += abs(correct_string.count('r')-produced_string.count('r'))
    off += abs(correct_string.count('s')-produced_string.count('s'))
    off += abs(correct_string.count('t')-produced_string.count('t'))
    off += abs(correct_string.count('u')-produced_string.count('u'))
    off += abs(correct_string.count('v')-produced_string.count('v'))
    off += abs(correct_string.count('w')-produced_string.count('w'))
    off += abs(correct_string.count('x')-produced_string.count('x'))
    off += abs(correct_string.count('y')-produced_string.count('y'))
    off += abs(correct_string.count('z')-produced_string.count('z'))
    
    error = (off/min_string_length)*100*0.5
    
    return error 

def hamming_distance(string1, string2): 
    # Start with a distance of zero, and count up
    distance = 0
    # Loop over the indices of the string
    L = min(len(string1),len(string2))
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
    # Return the final count of differences
    return distance