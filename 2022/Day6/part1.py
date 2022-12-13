from collections import Counter

def isUniqueChars(string):
 
    # Counting frequency
    freq = Counter(string)
 
    if(len(freq) == len(string)):
        return True
    else:
        return False

with open("input.txt") as file:
    signal = file.readline()
    for character in range(0,len(signal)-4):
        print(signal[character:character+4])
        if (isUniqueChars(signal[character:character+4])):
            print(character+4)
            break