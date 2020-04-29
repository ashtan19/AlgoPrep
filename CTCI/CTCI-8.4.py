# CTCI: 8.4 Power Set

# Time Complexity: Iter: n*2^n Recursive n*2^n
# Space Complexity: Iter: n*2^n Recursive: More than iterative
# Solving process:
# Problems Encountered: Creating a copy of a list must be done using element[:]

def PowerSetRecursive ( inputList, index ):
    
    #Base Case
    if (index == -1):
        powerset = []
        powerset.append([])
    else:
        powerset = PowerSetRecursive(inputList, index -1)
        # print(powerset)
        currentElement = inputList[index]
        currentSubsets = []
        for element in powerset:
            # print(element)
            newSubset = element[:]
            newSubset.append(currentElement)
            currentSubsets.append(newSubset)
        powerset +=currentSubsets
    return powerset


def PowerSet ( inputList ): #### INCORRECT####
    #Empty Set case
    if inputList == None: return -1
    if inputList == []: return inputList

    powerset  = []
    powerset.append([])
    start = 0
    count = 0
    while start < len(inputList):
        end = start + 1
        while end <= len(inputList):
            powerset.append(inputList[start:end])
            end += 1
            count += 1
        start += 1

    return powerset, count
    




testList = [1,2,3,4,5,6,7,8,9,10,11,12]
print(testList[len(testList)-1:len(testList)])


testList = [1,2,3,4,5,6,7]
print(PowerSet(testList))

# testList = ['a','b']
testList = [1,2,3,4,5,6,7]
subsetList = PowerSetRecursive(testList, len(testList) -1)
print(subsetList)
print(len(subsetList))
