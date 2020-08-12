"""
Leetcode: 339. Nested List Weight Sum

Attempts:1
Completed: Y
Acheived Ideal: Y

Time Complexity: O(n) where n is the number of integers in the nestedList and the depth
Space Complexity: O(depth)

Pattern: Recursion
Technique: 

Problems Encountered: The interface was not inuitive 
Other Solutions:

"""



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
'''
Process:
- RecursiveSum(nestedList, depth)
- Iterate through the nestedList 
- If element is an integer => sum += element * depth
- else: if it is a list => sum += recursiveSum(element, depth +1)
- return sum 

'''
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def recursiveSum(nestedList, depth):
            if nestedList == None or nestedList == []:
                return 0
            curSum = 0
            for element in nestedList:
                if element.isInteger():
                    curSum += element.getInteger() * depth
                else: 
                    curSum += recursiveSum(element.getList(), depth + 1)
            return curSum
                
        
        return recursiveSum(nestedList, 1)
    

        
        
        
        
        