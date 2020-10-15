"""
Leetcode: 5. Longest Palindromic Substring

Attempts: 1
Completed: Y
Acheived Ideal: Y, There is Manacher's Algorithm 
Under 30 Mins: Y

Time Complexity: O(n^2)
Space Complexity: O(1)

Pattern: Array Traversal and Palindrome
Technique: Expand from center at even element and check if palindrome

Problems Encountered: Ensure that you break out of the while loop if invalid
Other Solutions:

"""


'''
Idea:
    Iterate through s 
    At every element, we will expand to the sides and check if they are the same
    Also need to check between elements for palindromes
        if yes, increment sides of palindrome
        if no, return with start and end
    Track the largest palindrome and size
    
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s == '' or s == None:
            return ''

        longest_pal = s[0]
        max_pal_length = 1

        def check_sides(s, index, isOdd):
            count = 0
            l, r = -1, -1
            if isOdd:
                l, r = index-1, index+1
            else:
                l, r = index-1, index

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break

            return count

        for i in range(1, len(s)):
            odd = check_sides(s, i, True)
            even = check_sides(s, i, False)
            odd_pal_length = odd * 2 + 1
            even_pal_length = even * 2

            if odd_pal_length > even_pal_length and odd_pal_length > max_pal_length:
                longest_pal = str(s[i-odd: i+odd+1])
                max_pal_length = odd_pal_length
            else:
                if even_pal_length > max_pal_length:
                    longest_pal = str(s[i-even: i+even])
                    max_pal_length = even_pal_length

        return longest_pal
