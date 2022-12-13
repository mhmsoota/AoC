from collections import Counter

def isUniqueChars(string):
 
    # Counting frequency
    freq = Counter(string)
 
    if(len(freq) == len(string)):
        return True
    else:
        return False

with open("input.txt") as file:
    START_OF_MESSAGE_CHARACTERS = 14
    signal = file.readline()
    for i in range(0,len(signal)-START_OF_MESSAGE_CHARACTERS):
        print(signal[i:i+START_OF_MESSAGE_CHARACTERS])
        if (isUniqueChars(signal[i:i+START_OF_MESSAGE_CHARACTERS])):
            print(i+START_OF_MESSAGE_CHARACTERS)
            break