"""
Leetcode: LC 973 K Closest points to origin

Attempts: 1
Completed: N but got idea
Acheived Ideal:
Under 30 Mins: 

Time Complexity: O(nlogk)
Space Complexity: O(k)

Pattern: K most elements 
Technique: Heap or Sorting

Problems Encountered:
Other Solutions:

"""


class Solution:


def dist(self, ele):
    x = ele[0]
    y = ele[1]

    return math.sqrt(x**2 + y**2)  # can omit math.sqrt


def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    # given that len(points) cannot be null
    if len(points) == 0:  # we still check for edge case
        return None
    if len(points) == 1:  # if only one point exists then it must be the ans as K>=1
        return points

    maxheap = []  # stores negative dist and point in (x,y) format

    for point in points:  # O(n logk) #K <= n, so worst case is n logn
        # heappush is O(logk)
        heapq.heappush(maxheap, (-self.dist(point), point))

        # maintain heap size of K
        if len(maxheap) > K:
            # pop point with max dist #heappop is O(logk)
            heapq.heappop(maxheap)

    # now we are left with K no. of the smallest points in our maxheap as we kept on popping the points with the larger distance to origin

    # heapify has O(n). but to get our answer we would require to heappop 'K' times leading to O(n x logn). By using heappush and heappop method we can reduce it to O(nlogk) ~ O(nlogn)

    kclosest = []
    # copy out all points in maxheap as the ans, no need to use heappop for popping out in logK
    for pair in maxheap:  # O(n)
        kclosest.append(pair[1])  # add point to ans in any order

    return kclosest
