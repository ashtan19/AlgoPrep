
"""
Leetcode: 49. Group Anagrams

Attempts: 1
Completed: Y
Acheived Ideal: Y 
Under 30 Mins: Y

Time Complexity: O(n * nlogm) where m is longest string
Space Complexity: O(n)

Pattern: Sorting 
Technique: 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagramDict = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in anagramDict:
                anagramDict[sortedWord].append(word)
            else:
                anagramDict[sortedWord] = [word]

        return anagramDict.values()
