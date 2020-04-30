# CTCI: 1.6 String Compression

# Time Complexity: O(p + k^2) if using String Concat, O(n) if using array then convert to string
# Space Complexity: O(1) 3n
# Solving process:
# Problems Encountered: Needed to add the count of the last character outside the for loop

def StringCompression ( inputString ):
    if inputString == None: return None
    if inputString == "": return inputString

    compressed_string = []
    compressed_string.append(inputString[0])
    count = 1

    for i in range(1, len(inputString)):
        if inputString[i] == inputString[i-1]:
            count += 1
            # print ("same")
            # print(inputString[i])
            # print (i)

        else: # When the iterator encounters a different character
            # print("diff")
            # print(inputString[i])
            # print(i)
            compressed_string.append(str(count))
            compressed_string.append(inputString[i])
            count = 1 

    compressed_string.append(str(count))

    if (len(compressed_string) >= len(inputString)):
        return inputString 
    
    return ''.join(compressed_string)
    

print(StringCompression("aaaaabbbbcccdddeeeeeee"))
print(StringCompression(None))
print(StringCompression(""))
print(StringCompression("asdfgh"))