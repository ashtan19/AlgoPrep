"""
Leetcode: 349. Intersection of Two Arrays

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Pattern: Sets
Technique: Intersection of sets using & 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

#         if len(nums1) < len(nums2):
#             return self.intersection(nums2, nums1)

#         else:
#             table2 = Counter(nums2)
#             result = set()
#             for i in range(len(nums1)):
#                 if nums1[i] in table2:
#                     result.add(nums1[i])

#             return list(result)

        set1 = set(nums1)
        set2 = set(nums2)
        return set1 & set2
