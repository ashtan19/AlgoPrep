"""
Leetcode: 31. Next Permutation

Attempts: 1
Completed: N
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Array Manipulation 
Technique: Find the first ascending element from the back and then switch and reverse

Problems Encountered: Need to understand the problem really well and understand what the next permutation will be
Other Solutions:

"""


class Solution(object):
    def nextPermutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
