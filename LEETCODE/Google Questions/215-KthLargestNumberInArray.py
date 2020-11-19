"""
Leetcode: 215. Kth Largest Element in an Array

Attempts: 1
Completed: Y
Acheived Ideal: N 
Under 30 Mins: Y

Time Complexity: O(nlogk)
Space Complexity: O(k)

Pattern: K Largest  
Technique: Heap

Problems Encountered:
Other Solutions: Could just sort but O(nlogn). Could use quickselect for O(n)

"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq

        min_heap = []

        for i in range(len(nums)):
            if len(min_heap) < k:
                heapq.heappush(min_heap, nums[i])
                continue

            if min_heap[0] < nums[i]:
                heapq.heappushpop(min_heap, nums[i])

        return min_heap[0]

# Heap Solution but more concise


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]


# Quick select solution
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element

            # select a random pivot_index between
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)
