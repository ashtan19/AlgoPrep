"""
Leetcode: 1437. Check If All 1's Are at Least Length K Places Away

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: One Pass Count
Technique: 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        n = len(nums)
        num_zeros = 0
        seen_first_one = False

        for i in range(0, n):
            if nums[i] == 0:
                num_zeros += 1
                continue

            if seen_first_one == False:
                num_zeros = 0
                seen_first_one = True
                continue

            if num_zeros < k:
                return False

            num_zeros = 0

        return True
