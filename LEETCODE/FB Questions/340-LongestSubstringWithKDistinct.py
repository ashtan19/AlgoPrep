"""
Leetcode: 340. Longest Substring with At Most K Distinct Characters

Attempts: 1
Completed: Y 
Acheived Ideal: Y 
Under 30 Mins: No but close

Time Complexity: O(n)
Space Complexity: O(k) or O(1)

Pattern: Sliding Window
Technique: Expand the window until distinct chars surpass k, then shrink window

Problems Encountered:
Other Solutions: Can use a hashmap in to record the rightmost index of that char, then take the min of hashmap values to find the where you have to
                    get rid of one distinct char

"""


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s == None or s == "" or k == 0:
            return 0
        n = len(s)
        distinct, max_len, curr_len = 0, 0, 0
        char_dict = {}

        l = 0

        for r in range(0, n):
            c = s[r]
            if c not in char_dict or char_dict[c] == 0:
                distinct += 1
                char_dict[c] = char_dict.get(c, 0) + 1

                while distinct > k:
                    left = s[l]
                    char_dict[left] -= 1
                    curr_len -= 1
                    if char_dict[left] == 0:
                        distinct -= 1
                    l += 1
            else:
                char_dict[c] += 1

            curr_len += 1
            max_len = max(max_len, curr_len)

        return max_len


class Solution(object):

    """
    The general idea is to iterate over string s.
    Always put the character c and its location i in the dictionary d.
    1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
    2) Otherwise, we need to remove a character from the sliding window.
       Here's how to find the character to be removed:
       Because the values in d represents the rightmost location of each character in the sliding window, in order to find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret
