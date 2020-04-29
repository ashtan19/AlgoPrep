# CTCI: 10.4 Sorted Search, No Size

# Time Complexity: log(n)
# Space Complexity: n*logn
# Solving process: Recursively look through the array in log n time
# Problems Encountered: Keeping track of the currentIndex

# Another method is to use the same method to find an index that is too big. Then do a binary search using that index

#initialize currentIndex to be 1
def SortedSearchNoSize(inputList, x, currentindex):
    if inputList == None or inputList == []: return -1
    if inputList[currentindex] == x: return 0

    index = 1

    while (currentindex + index) <= len(inputList) and inputList[currentindex + index] <= x:
        if inputList[currentindex + index] == x: return index
        index *= 2
    
    return index/2 + SortedSearchNoSize(inputList, x, (currentindex + index/2))


testList = [0,1,2,3,4,5,6,7,8,9,10,11,12]

print(SortedSearchNoSize(testList, 9, 0))