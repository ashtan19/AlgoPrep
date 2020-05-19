# Leetcode: 22 Generate Parentheses

# Time Complexity: O(2^(2n) * n)
# Space Complexity: O(2^(2n) * n)
# Solving process:
# Problems Encountered:

# Other Solutions: Backtracking


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 0:
            return None
        elif n == 0:
            return []
        elif n == 1:
            return ["()"]
        else:
            hashtable = {}
            prevCombs = self.generateParenthesis(n-1)
            for comb in prevCombs:
                for i in range(0, len(comb)):
                    newComb = comb[:i] + "()" + comb[i:]
                    if newComb not in hashtable:
                        hashtable[newComb] = True
            return hashtable.keys()

# BackTracking Solution


class Solution(object):
    def generateParenthesis(self, N):
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
