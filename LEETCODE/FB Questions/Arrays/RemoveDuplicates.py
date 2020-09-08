'''
Question: LC 26 Remove Duplicates

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Two Pointers
Technique: 

'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        valid = 0
        if len(nums) > 1:
            for i in range(1, len(nums)):
                if nums[valid] == nums[i]:
                    continue
                else:
                    nums[valid + 1] = nums[i]
                    valid += 1
        return valid + 1
