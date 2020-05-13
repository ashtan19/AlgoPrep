# Leetcode: 338 Counting Bits

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solving process:
# Problems Encountered:

# Other Solutions:


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == None:
            return None
        numArr = [0] * (num+1)
        if num == 0:
            return numArr
        offset = 1
        for i in range(1, num+1):
            if offset * 2 == i:
                offset *= 2

            numArr[i] = numArr[i - offset] + 1

        return numArr
