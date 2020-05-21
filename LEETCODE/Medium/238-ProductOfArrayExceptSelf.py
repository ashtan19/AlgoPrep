# Leetcode: 238 Product of Array Except Self

# Time Complexity: O(3n)
# Space Complexity: O(3n)
# Acheived Ideal: No

# Solving process:
# Problems Encountered:

# Other Solutions: Contruct a forward array like before then just use one variable to keep track of
#                   running multiplication backwards and multiply with forward array


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == None:
            return None
        if nums == [] or len(nums) == 1:
            return []
        else:
            forward = nums[:]
            backward = nums[:]
            output = nums[:]
            for i in range(1, len(nums)):
                forward[i] = nums[i] * forward[i-1]
            for i in range(len(nums)-2, -1, -1):
                backward[i] = nums[i] * backward[i+1]
            for i in range(len(nums)):
                if i-1 >= 0 and i+1 < len(nums):
                    output[i] = forward[i-1] * backward[i+1]
                elif i-1 < 0:
                    output[i] = backward[i+1]
                elif i+1 >= len(nums):
                    output[i] = forward[i-1]
            return output


# Space of O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0]*length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
