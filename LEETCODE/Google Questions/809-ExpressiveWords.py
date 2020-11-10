
"""
Leetcode: 809 Expressive Words

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: N

Time Complexity: O(n*k) where k is the longest word
Space Complexity: O(S)

Pattern: Iteration 
Technique: 

Problems Encountered:
Other Solutions: Can use itertools

"""


class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        def get_count(S):
            result = []
            for i in range(len(S)):
                if i == 0:
                    result.append((S[i], 1))
                    continue
                prev_char, count = result[-1]
                if S[i] == prev_char:
                    result[-1] = (prev_char, count + 1)
                else:
                    result.append((S[i], 1))
            return result

        s_count = get_count(S)
        result = 0

        for word in words:
            word_count = get_count(word)
            if len(word_count) != len(s_count):
                continue

            is_stretchy = True
            for i in range(len(s_count)):
                w_char, w_num = word_count[i]
                s_char, s_num = s_count[i]
                not_stretchy = w_char != s_char or w_num > s_num or (
                    w_num < s_num and s_num < 3)
                if not_stretchy:
                    is_stretchy = False
                    break
            if is_stretchy:
                result += 1

        return result


class Solution(object):
    def expressiveWords(self, S, words):
        def RLE(S):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R:
                continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))

        return ans
