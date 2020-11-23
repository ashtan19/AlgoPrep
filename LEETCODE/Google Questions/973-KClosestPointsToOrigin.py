"""
Leetcode: 973. K Closest Points to Origin

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(nlogk)
Space Complexity: O(k)

Pattern: Min K elements
Technique: Use a max heap to keep track of the k closest elements

Problems Encountered:
Other Solutions: Can use quick select to get an average O(n) time[worst case O(n^2)] and O(n) space 

"""


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        closest = []

        for point in points:
            distance = -(point[0]**2 + point[1]**2)
            if len(closest) < K or closest[0][0] <= distance:
                heapq.heappush(closest, (distance, point))

            if len(closest) > K:
                heapq.heappop(closest)

        return [point[1] for point in closest]
