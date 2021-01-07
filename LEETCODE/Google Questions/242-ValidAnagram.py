"""
Leetcode: 242. Valid Anagram

Attempts: 1
Completed: Y
Acheived Ideal: Y use hashtable for O(n) but extra space
Under 30 Mins: Y

Time Complexity: O(nlogn)
Space Complexity:

Pattern: 
Technique: 

Problems Encountered:
Other Solutions: 

"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return sorted(s) == sorted(t)
