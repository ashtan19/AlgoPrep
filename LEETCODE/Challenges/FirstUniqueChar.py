# May Challenge May 7th First Unique Character in a String
# Time : O(n)

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0: return -1
        charMap = {}
        for index, char in enumerate(s):
            if char in charMap: 
                charMap[char][1] += 1
            else:
                charMap[char] = [index, 1]
        firstCharIndex = len(s)
        for charCount in charMap.values():
            if charCount[1] == 1 and charCount[0] < firstCharIndex:
                firstCharIndex = charCount[0]
        if firstCharIndex == len(s):
            return -1
        return firstCharIndex


#Cleanest Solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1