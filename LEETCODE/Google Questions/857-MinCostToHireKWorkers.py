"""
Leetcode: 857. Minimum Cost to Hire K Workers

Attempts: 1
Completed: N
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(NlogN)
Space Complexity: O(N)

Pattern: Min K Elements 
Technique: Use the ratio of wage/quality to sort the workers. Use a heap to keep track of the K highest quality 
            workers. We want to get rid of highest quality workers because they increase the total cost

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """

        workers = sorted(((float(w)/float(q)), q, w)
                         for q, w in zip(quality, wage))

        result = float("inf")
        group = []
        quality_sum = 0

        for ratio, q, w in workers:
            heapq.heappush(group, -q)  # Maintain a maxheap of quality
            quality_sum += q

            if len(group) > K:
                quality_sum += heapq.heappop(group)

            if len(group) == K:
                result = min(result, ratio * quality_sum)

        return result
