# Leetcode: 347 Get top K frequent elements

# Time Complexity: O(nlogn) if we use sort.
# Space Complexity: O(3n)
# Solving process: Get frequency of each element. Create hashtable of count:[elems]. Create
#                   sorted list of elements, return the k elements
# Problems Encountered:

# Other Solutions: Use a heap


import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        elemFreq = collections.Counter(nums)
        countDict = {}
        sortedElems = []
        for elem in elemFreq.keys():
            if elemFreq[elem] in countDict:
                countDict[elemFreq[elem]].append(elem)
            else:
                countDict[elemFreq[elem]] = [elem]
        print(countDict)
        print(countDict.keys())
        sortedCount = sorted(countDict.keys())
        print(sortedCount)
        for i in range(len(sortedCount)-1, -1, -1):
            sortedElems.extend(countDict[sortedCount[i]])

        return sortedElems[:k]


testSolution = Solution()
testCase = [1, 1, 1, 2, 2, 3]
print(testSolution.topKFrequent(testCase, 2))

print(testCase[len(testCase)-1:len(testCase)])

# #Heap Solution
# class Solution:
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         count = collections.Counter(nums)
#         return heapq.nlargest(k, count.keys(), key=count.get)
