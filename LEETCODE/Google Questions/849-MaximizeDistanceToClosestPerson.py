

"""
Leetcode: 849. Maximize Distance to Closest Person

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Array and pointer
Technique: Keep track of the last occupied seat and take the distance divided by 2 unless you are at the ends of row

Problems Encountered:
Other Solutions: Two Pointers

"""


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_distance = 1
        last_taken = -1
        n = len(seats)

        for i in range(n):
            if i == n-1 and seats[i] == 0:
                max_distance = max(max_distance, i - last_taken)
                break

            if seats[i] == 1:
                if last_taken == -1:
                    max_distance = max(max_distance, i)
                else:
                    max_distance = max(max_distance, (i-last_taken) // 2)

                last_taken = i

        return max_distance


# Two Pointer Solution
class Solution(object):
    def maxDistToClosest(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans
