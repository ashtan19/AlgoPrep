# Leetcode: 560. Subarray Sum Equals K

# Attempts: 1
# Completed: Y
# Acheived Ideal: N

# Time Complexity: O(n^2)
# Space Complexity:

# Solving process: Running sum
# Problems Encountered:

# Other Solutions: Use a hashmap to keep track of diffences in running sum

# Brute Force
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        result = 0
        for i in range(0, len(nums)):
            currsum = 0
            for j in range(i, len(nums)):
                currsum += nums[j]
                if currsum == k:
                    result += 1

        return result

# Hashmap solution O(n) time and space


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k, 0)
            d[sums] = d.get(sums, 0) + 1

        return(count)
