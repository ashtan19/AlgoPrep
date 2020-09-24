"""
Leetcode: 238. Product of Array Except Self

Attempts: 1
Completed: N 
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Array Manipulation and pointers
Technique: The value of index i is determined by the product of the left side and right side of it. So precalculate the 
            left sides and right sides and then multiply them

Problems Encountered: Difficult to come up with the technique
Other Solutions: Can optimize to only use the result array

"""

# Best Solution using O(n) Time and O(1) space


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0]*n
        result[n-1] = 1
        left_product = 1

        for i in range(1, n):
            result[n-1-i] = result[n-i] * nums[n-i]

        for i in range(1, n):
            left_product *= nums[i-1]
            result[i] *= left_product

        return result

# Time O(n) Space O(n) Solution


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_array = [0]*n
        right_array = [0]*n
        left_array[0], right_array[n-1] = 1, 1
        result = []

        for i in range(1, n):

            left_array[i] = left_array[i-1] * nums[i-1]
            right_array[n-1-i] = right_array[n-i] * nums[n-i]

        for i in range(0, n):
            result.append(left_array[i] * right_array[i])

        return result
