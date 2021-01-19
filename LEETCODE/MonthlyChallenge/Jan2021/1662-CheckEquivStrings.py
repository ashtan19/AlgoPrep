"""
Leetcode:1662. Check If Two String Arrays are Equivalent

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: String (Dumb Question)
Technique: 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """

        return "".join(word1) == "".join(word2)
