"""
Leetcode: 76. Minimum Window Substring (Hard)

Attempts: 1
Completed: N
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Sliding Window 
Technique: Sliding window question but need to keep track of number of formed letters, letters in window, min window

Problems Encountered: Tough to figure out in the first try
Other Solutions: There is another method of filtering the letters in s that occur in t but it is challenging

"""

'''
Algorithm: 
1) Collections.counter(T), lettersFormed = int, windowLetters = {}
2) Have two pointers that start at the start of S
3) For loop that increments R pointer
    if the char at R is in Tdict:
        if L is None => set L to R
        set Tdict(S[R]) -= 1, n -= 1
        if L = R and Tdict(S[R]) < 0:
            L += 1
            Tdict(S[R]) += 1, n+= 1
            while S[L] not in Tdict:
                L += 1

'''


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if s == "" or t == "":
            return ""

        dictT = collections.Counter(t)
        TUnique = len(dictT)
        lettersFormed = 0
        windowLetters = {}
        minWindow, minL, minR = float("inf"), 0, 0

        L, R, = 0, 0

        while R < len(s):
            RLetter = s[R]
            if RLetter in dictT:
                RCount = windowLetters.get(RLetter, 0) + 1
                windowLetters[RLetter] = RCount
                if RCount == dictT[RLetter]:
                    print("hello")
                    lettersFormed += 1

                    while lettersFormed == TUnique:
                        if R-L < minWindow:
                            minWindow, minL, minR = R-L, L, R
                        LLetter = s[L]
                        if LLetter in dictT:
                            LCount = windowLetters[LLetter] - 1
                            windowLetters[LLetter] = LCount
                            if LCount < dictT[LLetter]:
                                lettersFormed -= 1
                        L += 1
            R += 1

        return s[minL:minR + 1] if minWindow <= len(s) else ""
