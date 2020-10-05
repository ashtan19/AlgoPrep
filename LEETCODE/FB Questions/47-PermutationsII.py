"""
Leetcode:47. Permutations II

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(N*N!)
Space Complexity: O(N*N!)

Pattern: recursion
Technique: Backtracking 

Problems Encountered: Cannot use original method to backtrack
Other Solutions: Pass a counter of unique nums and iterate over unique elements instead of all elements

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None or nums == []:
            return [nums]

        result = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                result.append(comb[:])
                return

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))
        return result
