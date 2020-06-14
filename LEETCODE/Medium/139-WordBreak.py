# Leetcode: 139 Word Break

# Attempts:1
# Completed: N
# Acheived Ideal: N

# Time Complexity: O(nm)
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions: Use DP

# DP solution
def word_break(s, words):
    d = [False] * len(s)
    for i in range(len(s)):
        for w in words:
            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                d[i] = True
    return d[-1]



# This solution only works for dicts with words that have no other prefix words
'''
Input: 
    s - > string
    wordDict -> list of strings 
    
Sample: 
s = "leetcodee", wordDict = ["leet", "code"]
s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
substring= ""

wordhash = dictionary of all the words
substring = ''

Logic: 
1) Convert worddict list into wordhash
2) Iterate through s and add characters to substring via concatentation
3) If substring matches word in wordhash -> substring = ''
4) After loop, check if substring is "" -> if yes return true else False

'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s == None or s == '' or wordDict == None or wordDict == []:
            return False

        def convert_to_dict(wordlist):
            wordhash = {}
            for word in wordlist:
                wordhash[word] = None
            return wordhash

        wordhash = convert_to_dict(wordDict)
        substring = ''
        for char in s:
            substring += char
            print(substring)
            if substring in wordhash:
                substring = ''

        return substring == ''
