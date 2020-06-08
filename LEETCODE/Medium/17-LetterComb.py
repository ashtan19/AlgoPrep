# Leetcode: 17. Letter Combinations of a Phone Number

# Attempts: 1
# Completed: 1
# Acheived Ideal: Y

# Time Complexity: 4^n
# Space Complexity: n^2

# Solving process: Recursive and Memo
# Problems Encountered:

# Other Solutions: Could also do bottom up approach


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if digits == "" or digits == None:
            return []
        return self.findComb(digits)

    def findComb(self, digits):
        if digits in self.mapping:
            return self.mapping[digits]
        suffix = digits[1:]
        if suffix in self.mapping:
            suffixarr = self.mapping[suffix]
        else:
            suffixarr = self.findComb(suffix)
        result = []
        for letter in self.mapping[digits[0]]:
            for suffixelem in suffixarr:
                result.append(letter + suffixelem)

        self.mapping[digits] = result

        return result
