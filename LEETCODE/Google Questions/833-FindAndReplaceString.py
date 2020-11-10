"""
Leetcode: 833 Find and Replace in String

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n * k) where k is num replacements
Space Complexity: O(n)

Pattern: String manipulation
Technique: Do the replacements in reverse index order to preserve the index invariant 

Problems Encountered:
Other Solutions: Can be done with zip for fewer lines of code 

"""


class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """

        replacements = []
        for i in range(len(indexes)):
            replacements.append((indexes[i], sources[i], targets[i]))
        replacements.sort(reverse=True)

        def check_matching(S, source, index):
            if index + len(source) <= len(S) and S[index: index+len(source)] == source:
                return True
            return False

        for i in range(len(replacements)):
            index, source, target = replacements[i]
            if check_matching(S, source, index):
                S = S[:index] + target + S[index + len(source):]

        return S
