"""
Leetcode:523. Continuous Subarray Sum

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(n^2) can be O(n)
Space Complexity: O(n) can be O(min(n,k))

Pattern: DP
Technique: Running Sum 

Problems Encountered: 
Other Solutions: 

"""


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        running_sum = [0] * (len(nums)+1)
        curr_sum = 0
        for i in range(len(nums)):
            running_sum[i] = curr_sum
            curr_sum += nums[i]
        running_sum[-1] = curr_sum

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if k == 0 and (running_sum[j+1] - running_sum[i]) == 0:
                    return True
                elif k != 0 and (running_sum[j+1] - running_sum[i]) % k == 0:
                    return True

        return False


class Solution(object):
    def checkSubarraySum(self, nums, k):
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in xrange(len(nums) - 1))
        mods, cum_sum_mod_k = {0: -1}, 0
        for i, n in enumerate(nums):
            cum_sum_mod_k = (cum_sum_mod_k + n) % k
            if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
                return True
            if cum_sum_mod_k not in mods:
                mods[cum_sum_mod_k] = i
        return False
