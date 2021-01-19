"""
Leetcode:881. Boats to Save People

Attempts:1
Completed:Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(nlogn) => sorting
Space Complexity: O(1) => assuming sorting is in place

Pattern: Two Pointer
Technique: Sort the array, then check if weight over limit, if yes only decrement right

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort()

        n = len(people)
        left, right = 0, n-1
        boats = 0

        while left <= right:
            if left == right:
                boats += 1
                break

            left_weight = people[left]
            right_weight = people[right]
            if left_weight + right_weight > limit:
                right -= 1
            else:
                right -= 1
                left += 1
            boats += 1

        return boats

# Cleaner solution


class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans
