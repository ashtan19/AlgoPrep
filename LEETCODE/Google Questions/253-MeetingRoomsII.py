"""
Leetcode: 253. Meeting Rooms II

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: N

Time Complexity: O(nlogn) b/c of sort and possibly heap
Space Complexity: O(n) because of the heap 

Pattern: Interval question 
Technique: Sort the array and then keep track of the number of occupied rooms.
            If the current meeting start time is after the min heap end time, replace it

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        import heapq
        num_rooms = []
        max_rooms = 0

        # intervals = sorted(intervals, key=lambda x: x[0])
        intervals.sort()

        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if not num_rooms or num_rooms[0] > start:
                heapq.heappush(num_rooms, end)
            else:
                heapq.heappushpop(num_rooms, end)
            max_rooms = max(max_rooms, len(num_rooms))

        return max_rooms
