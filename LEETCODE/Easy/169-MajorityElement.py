# Leetcode: 169 Majority Element

# Attempts:2
# Completed: Y
# Acheived Ideal: Y

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Solving process: Sort then take middle element
# Problems Encountered:

# Other Solutions: Boyer-Moore Algo


# Attempt 2
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        return nums[len(nums)/2]

# Boyer-Moore


class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
