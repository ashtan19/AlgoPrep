# Leetcode: 96. Unique Binary Search Trees

# Completed: Y
# Acheived Ideal: Y (for time complexity)

# Time Complexity: O(n) b/c of memo
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions: DP


# Recursive Addition with Memo (Very fast)
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.treetable = {0: 1, 1: 1, 2: 2}
        return self.uniqueTrees(n)

    def uniqueTrees(self, n):
        if n in self.treetable:
            return self.treetable[n]
        sum = 0
        for i in range(0, n):
            sum += self.uniqueTrees(i) * self.uniqueTrees(n-1-i)
        self.treetable[n] = sum

        return sum

# Dynamic Programming O(n^2) O(n)


class Solution(object):
    def numTrees(self, n):
        res = [0] * (n+1)
        res[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
