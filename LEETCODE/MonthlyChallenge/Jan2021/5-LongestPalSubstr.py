"""
Leetcode:5. Longest Palindromic Substring

Attempts: 1
Completed: Y
Acheived Ideal: Yes
Under 30 Mins: Y

Time Complexity: O(n^2)
Space Complexity: O(1)

Pattern: Palindrome String
Technique: Expand around center

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def check_pal(s, index, is_odd):
            left = index - 1 if is_odd else index
            right = index + 1

            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1

            return (left+1, right-1)

        max_string = ""
        max_len = -1  # set to -1 to account for 1 char in odd, can also add 1 to odd & even len
        for i in range(len(s)):
            odd_left, odd_right = check_pal(s, i, True)
            even_left, even_right = check_pal(s, i, False)
            # print(odd_left, odd_right, even_left, even_right)
            odd_len = odd_right - odd_left
            even_len = even_right - even_left
            if odd_len > max_len:
                max_string = s[odd_left:odd_right+1]
                max_len = odd_len
            if even_len > max_len:
                max_string = s[even_left: even_right+1]
                max_len = even_len

        return max_string
