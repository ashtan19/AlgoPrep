# CTCI-10.2 Grouping anagrams
# O(n * average characters in each string + n^2)
# Solving process: 1) Convert strings into hashtables(dicts) then compare hash tables in the list of hashtables and add them to output list if yes

def groupAnagrams(inputStringList):
    
    stringHashs = []
    for sentence in inputStringList:
        sentenceHash = {}
        for c in sentence:
            if c in sentenceHash: sentenceHash[c] += 1
            else: sentenceHash[c] = 1

        stringHashs.append(sentenceHash)
    
    outputArr = []

    for j in range(0, len(stringHashs)):
        if stringHashs[j]:
            outputArr.append(inputStringList[j])

            for i in range(j+1, len(stringHashs)):

                if stringHashs[j] == stringHashs[i]:
                    outputArr.append(inputStringList[i])
                    stringHashs[i] = None
    
    return outputArr


testStringlist = ["dog", "cat", "god", "goot", "tac", "123456", "toog", "654321"]

print(groupAnagrams(testStringlist))

