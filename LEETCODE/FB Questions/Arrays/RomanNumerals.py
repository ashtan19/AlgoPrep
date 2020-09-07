'''
Question: 13. Roman to Integer

Time Complexity: O(1) because capped at 3999
Space Complexity: O(1)

Pattern: Array Sliding Window
Technique: Can also process from right to left
'''


'''
1) Dictionary of the values M, C, X, I
2) If len(s) is equal to 1: we want to return that converted char value
3) while loop that loops till n-2
4) Check the current value and the next value. If the next value is greater than current value
    we will subtract current value from next value and add it to result and add two to index
    else: we will add current value and add 1 to index
5) return result
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        chardict = {"M": 1000, "D": 500, "C": 100,
                    "L": 50, "X": 10, "V": 5, "I": 1}
        result, index = 0, 0

        if len(s) == 1:
            return chardict[s]

        while index < len(s):
            curChar = s[index]
            if index < len(s)-1:
                nextChar = s[index + 1]
                if chardict[nextChar] > chardict[curChar]:
                    result += chardict[nextChar] - chardict[curChar]
                    index += 2
                    continue
            result += chardict[curChar]
            index += 1

        return result
