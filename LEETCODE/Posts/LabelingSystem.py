"""
Leetcode: Amazon OA 2029 Labeling System
Link: https://leetcode.com/discuss/interview-question/893442/

Attempts: 1
Completed: N but got right idea
Acheived Ideal:
Under 30 Mins:

Time Complexity: O(n)
Space Complexity:

Pattern:
Technique: Use an array/hashtable to hold the char count of each char and then ensure that you
            the right number of chars of the current biggest char and add buffers of next biggest char

Problems Encountered:
Other Solutions:

"""


def largest(string, k):
    counts = [0] * 26

    for c in string:
        counts[ord(c) - ord('a')] += 1

    res = ""

    for i in reversed(range(26)):
        while counts[i]:
            add = min(counts[i], k)

            # append `add` characters to result
            counts[i] -= add
             res += chr(ord('a') + i) * add

              if counts[i]:
                   # add 1 of next largest
                   for j in reversed(range(i)):
                        if counts[j]:
                            counts[j] -= 1
                            res += chr(ord('a') + j)
                            break
                    else:
                        return res

    return res
