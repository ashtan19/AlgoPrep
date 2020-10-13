
"""
Leetcode: 350. Intersection of Two Arrays II

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n + m)
Space Complexity: O(n)

Pattern: Sets
Technique: Use hashtable

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)
        else:
            table2 = Counter(nums1)
            result = []
            for i in range(0, len(nums2)):
                if nums2[i] in table2:
                    result.append(nums2[i])
                    table2[nums2[i]] -= 1
                    if table2[nums2[i]] == 0:
                        del table2[nums2[i]]

            return result
