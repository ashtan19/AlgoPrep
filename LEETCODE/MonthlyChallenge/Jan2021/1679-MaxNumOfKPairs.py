"""
Leetcode:1679. Max Number of K-Sum Pairs

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(n) Two Pass
Space Complexity: O(n)

Pattern: Array
Technique: Use Hashmap to count the number of unique nums and find compliment

Problems Encountered:
Other Solutions: Can do in one pass while building the hashmap

"""


# Two Pass
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        from collections import Counter

        num_table = Counter(nums)
        result = 0

        for num in num_table.keys():
            comp = k - num
            if comp not in num_table:
                continue
            if comp == num:
                result += num_table[num] // 2
                num_table[num] = 0
                continue

            comp_count = num_table[comp]
            num_count = num_table[num]

            result += min(comp_count, num_count)

            num_table[num] = 0
            num_table[comp] = 0

        return result

# One Pass


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        num_table = {}
        result = 0

        for num in nums:
            comp = k - num
            if comp not in num_table:
                num_table[num] = num_table.get(num, 0) + 1
                continue

            result += 1
            num_table[comp] -= 1
            if num_table[comp] == 0:
                del num_table[comp]

        return result
