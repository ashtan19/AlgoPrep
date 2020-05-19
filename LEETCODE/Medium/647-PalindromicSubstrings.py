# Leetcode: 647 Palindromic Substrings

# Time Complexity: O(n^3)
# Space Complexity: O(n) cuz of isPalindrome
# Acheived Ideal: No

# Solving process:
# Problems Encountered:

# Other Solutions:  1) Expand around center O(n^2), O(1)
#                   2) Manacher's Algorithm O(n), O(n) ## Tough to implement in interview setting


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == '' or s == None:
            return 0
        palincount = 0
        for substrlen in range(1, len(s)+1):
            for i in range(0, len(s)):
                if i + substrlen <= len(s):
                    if self.isPalindrome(s[i:i+substrlen]):
                        palincount += 1
        return palincount

    def isPalindrome(self, substring):
        return substring == substring[::-1]


# Expand Around center
class Solution(object):
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in xrange(2*N - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

# Manachers


def countSubstrings(self, S):
    def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        Z = [0] * len(A)
        center = right = 0
        for i in xrange(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i + Z[i]
        return Z

    return sum((v+1)/2 for v in manachers(S))
