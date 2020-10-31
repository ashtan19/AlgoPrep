"""
Leetcode: Amazon OA Chemical Delivery System
Link: https://leetcode.com/discuss/interview-question/893279/

Attempts: 1
Completed: N but got right approach
Acheived Ideal:
Under 30 Mins: 

Time Complexity: O(num flasks * requirements * log(markings))
Space Complexity: O(markings)

Pattern: Searching 
Technique: Binary Search on markings of each flask

Problems Encountered:
Other Solutions:

"""


from collections import defaultdict


class Solution:
    # binary search to find the "right larger than or equal to" element than target, will keep looking for exact match
    def binSearch(self, nums, left, right, target, closestMark):

        # unsuccessful search, return closest match
        if left > right:
            return closestMark

        mid = (left+right)//2

        # closest match to target was found
        if nums[mid] >= target and nums[mid] < closestMark:
            closestMark = nums[mid]

        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] > target:
            return self.binSearch(nums, left, mid-1, target, closestMark)
        else:
            return self.binSearch(nums, mid+1, right, target, closestMark)

    def foo(self, numOrders, requirements, flaskTypes, totalMarks, markings):
        # store the markings of each flask in a list (they are already sorted) to make binary search feasible
        markingsHt = defaultdict(list)
        for m in markings:
            markingsHt[m[0]].append(m[1])

        # compute the total waste for each flask
        minWaste, ret = float('inf'), -1
        for flask in markingsHt:
            waste = 0
            for r in requirements:
                curWaste = self.binSearch(markingsHt[flask], 0, len(
                    markingsHt[flask])-1, r, float('inf'))
                waste += curWaste-r
                if curWaste == float('inf'):
                    break

            # solution is feasible and better than existing one (less waste)
            if waste != float('inf') and waste < minWaste:
                minWaste, ret = waste, flask

        return ret
