"""
Leetcode: 884 BackspaceStringCompare

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: String Comparision 
Technique: Iterate from the back and check if the chars are the same 

Problems Encountered:
Other Solutions: Can use a generator to yield the current char from each string to compare

"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        index_s = len(S) - 1
        index_t = len(T) - 1

        while index_s >= 0 or index_t >= 0:
            char_s = ""
            char_t = ""
            backspace_s, backspace_t = 0, 0
            while index_s >= 0:
                if S[index_s] != "#" and backspace_s == 0:
                    char_s = S[index_s]
                    break
                backspace_s = backspace_s + \
                    1 if S[index_s] == "#" else backspace_s-1
                index_s -= 1

            while index_t >= 0:
                if T[index_t] != "#" and backspace_t == 0:
                    char_t = T[index_t]
                    break
                backspace_t = backspace_t + \
                    1 if T[index_t] == "#" else backspace_t-1
                index_t -= 1

            if char_s != char_t:
                return False

            index_s -= 1
            index_t -= 1

        return True

# Generator Solution


class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
