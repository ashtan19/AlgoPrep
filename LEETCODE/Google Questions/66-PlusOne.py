"""
Leetcode: 66. Plus One

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Array Traversal
Technique: 

Problems Encountered:
Other Solutions:

"""


'''
Idea:
    - Add 1 to last element of digits
    - Iterating from n-1 to 1:
        if element is 10: 
            nums[i] = 0
            nums[i-1] += 1
    
            
    If digits[0] == 10:
        digits[0] = 0
        return [1] + [digits]
    
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits[-1] += 1

        for i in range(len(digits)-1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
            else:
                return digits

        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        else:
            return digits
