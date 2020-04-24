#CTCI 1.4 Palindrome Permutation
#O(n)

def palPerm (inputString):
    
    if inputString == None: return False
    if len(inputString) == 0 : return True

    lowerStr = inputString.lower().replace(" ", "")
    print(lowerStr)

    charHash = {}

    for x in lowerStr:
        if x in charHash: charHash[x] += 1
        else: charHash[x] = 1
    print(charHash)
    if len(lowerStr) % 2 == 0:  
        return all(value % 2 == 0 for value in charHash.values())
    
    else: 
        counter = 0
        for value in charHash.values():
            if value % 2 == 1 : counter += 1
        if counter > 1: return False
        else: return True

print(palPerm("HaN na    h")) 