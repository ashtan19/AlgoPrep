"""
Leetcode: 247. Strobogrammatic Number II

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(5^n)
Space Complexity: O(5^n)

Pattern: Recursion
Technique: 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def findComb(n, m):
            if m == 0:
                return [""]
            if m == 1:
                return ["0", "1", "8"]

            combos = findComb(n, m-2)

            result = []

            for i in range(len(combos)):
                s = combos[i]
                if n != m:
                    result.append("0" + s + "0")
                result.append("6" + s + "9")
                result.append("9" + s + "6")
                result.append("8" + s + "8")
                result.append("1" + s + "1")

            return result

        return findComb(n, n)


# My first solution - Slow
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pairs = {"6": "9", "9": "6", "1": "1", "8": "8", "0": '0'}
        first_pairs = {"6": "9", "9": "6", "1": "1", "8": "8"}
        ones = {"1": "1", "8": "8", "0": "0"}
        result = []

        def findComb(left, right, rem):
            if rem == 0:
                result.append("".join(left[:] + right[::-1]))
                return
            elif rem == 1:
                for num in ones:
                    result.append("".join(left[:] + [ones[num]] + right[::-1]))
                return
            else:
                if rem == n:
                    for num in first_pairs:
                        left.append(num)
                        right.append(first_pairs[num])
                        findComb(left, right, rem-2)
                        left.pop()
                        right.pop()
                else:
                    for num in pairs:
                        left.append(num)
                        right.append(pairs[num])
                        findComb(left, right, rem-2)
                        left.pop()
                        right.pop()

        if n == 1:
            return ["1", "8", "0"]
        findComb([], [], n)
        return result
