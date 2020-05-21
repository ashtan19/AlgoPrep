# Leetcode: 49 Group Anagrams

# Time Complexity: O(n KlogK) where K is the longest string
# Space Complexity: O(nK)
# Acheived Ideal: No O(nK)

# Solving process:
# Problems Encountered:

# Other Solutions: strings are anagrams if their character count is the same. So Generate a char count
#                   of each string in O(nK)


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None:
            return None
        if strs == []:
            return []
        else:
            strsCopy = strs[:]
            strsDict = {}
            for i in range(len(strsCopy)):
                strsCopy[i] = "".join(sorted(strsCopy[i]))
                if strsCopy[i] in strsDict:
                    strsDict[strsCopy[i]].append(strs[i])
                else:
                    strsDict[strsCopy[i]] = [strs[i]]

            return strsDict.values()


# Char Count
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
