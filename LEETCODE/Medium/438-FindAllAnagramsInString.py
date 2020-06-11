# Leetcode: 438. Find All Anagrams in a String

# Attempts: 1
# Completed: Y
# Acheived Ideal: N

# Time Complexity: O(n * nlogn)
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions: Sliding Window O(n) b/c only 26 chars in dictionary



# Brute Force
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        plist = sorted(list(p))
        slist = list(s)
        anagramlen = len(p)
        result = []
        if s == '' or s == None or p == ''or p == None:
            return result

        for i in range(0, len(s)-anagramlen+1):
            substring = sorted(slist[i:i+anagramlen])
            if substring == plist:
                result.append(i)

        return result

# Sliding Window


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pCount = collections.Counter(p)
        sCount = collections.Counter(s[:len(p)-1])
        result = []

        for i in range(len(p)-1, len(s)):
            sCount[s[i]] += 1
            if sCount == pCount:
                result.append(i-len(p)+1)
            sCount[s[i-len(p)+1]] -= 1
            if sCount[s[i-len(p)+1]] == 0:
                del sCount[s[i-len(p)+1]]

        return result
