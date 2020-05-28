# Leetcode:621. Task Scheduler

# Completed: N
# Acheived Ideal:

# Time Complexity: O(n)
# Space Complexity: O(1)

# Solving process:
# Problems Encountered: Really Tough...

# Other Solutions: Sorting, Heap(Priority Queue), Calculate Idle Slots


from heapq import heappush, heappop
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        curr_time, h = 0, []
        for k, v in Counter(tasks).items():
            heappush(h, (-1*v, k))
        while h:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if h:
                    x, y = heappop(h)
                    if x != -1:
                        temp.append((x+1, y))
                if not h and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(h, item)
        return curr_time
