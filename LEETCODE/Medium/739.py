# Leetcode: 739 Daily Temperatures

# Time Complexity: O(n^2)
# Space Complexity: (n)
# Solving process:
# Problems Encountered: Tried to Sort but it was not useful

# Other Solutions: Use a stack

# Brute Force O(N^2) solution.
#


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if T == []:
            return []
        if len(T) == 1:
            return [0]
        result = [0] * len(T)

        for i in range(0, len(T)-1):
            for j in range(i+1, len(T)):
                if T[j] > T[i]:
                    result[i] = (j-i)
                    break

        return result

# O(n) Solution Using a stack to keep track of biggest temperatures


class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []  # indexes from hottest to coldest
        for i in xrange(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
