"""
Leetcode: 896. Monotonic Array

Attempts: 1
Completed: Y 
Acheived Ideal: Y

Time Complexity: O(N)
Space Complexity: O(1)

Pattern: Array Traversal
Technique: There is a two pass(Slow) where you check for increasing then check for decreasing
            or check once like below

Problems Encountered:
Other Solutions:

"""



class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 2: 
            return True
        isIncrease = A[0] < A[-1]
        
        for i in range(0, len(A)-1):
            if (isIncrease and A[i] > A[i+1]) or (not isIncrease and A[i] < A[i+1]):
                return False
            
        return True
        