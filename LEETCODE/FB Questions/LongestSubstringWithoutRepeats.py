'''
Question:   Longest Substring Without Repeating Characters

Time Complexity: O(n)
Space Complexity: O(1) because there are only 26 chars possible 

Pattern: Sliding Window
Technique: 

'''

'''
Algorithm: Sliding Window
1) Expand end pointer
2) Checking if current element is in hashtable 
    No: Add to hashtable, check against max length
    Yes: while hashtable[currElement] exists => delete that start element from hashtable
        add the current element and check for max value
3) Return Max value

s = "abcabcbb"
n = 8
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        start, maxlen = 0, 0
        chars = {}

        for end in range(0, n):
            while s[end] in chars:
                del chars[s[start]]
                start += 1
            chars[s[end]] = True
            maxlen = max(maxlen, len(chars))

        return maxlen
