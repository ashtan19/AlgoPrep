"""
Leetcode: 986. Interval List Intersections

Attempts: 2
Completed: Y
Acheived Ideal: Y 
Under 30 Mins: Y

Time Complexity: O(m+n)
Space Complexity: O(m+n)

Pattern: Intervals
Technique: When comparing two intervals, take the max of starts and min of ends 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        indexA, indexB = 0, 0
        result = []

        while indexA < len(A) and indexB < len(B):
            startA, endA = A[indexA][0], A[indexA][1]
            startB, endB = B[indexB][0], B[indexB][1]
            resStart = max(startA, startB)
            resEnd = min(endA, endB)
            if resEnd >= resStart:
                result.append([resStart, resEnd])
            if endA <= endB:
                indexA += 1
            else:
                indexB += 1

        return result
