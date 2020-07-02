"""
Question: Top 'K' Numbers (easy)

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Top K Elements 
Technique: First add k elements into the heap. Then when we encounter a new element that is larger than
            the min of the heap, we pop the heap and then push in the new element. We will keep only k elements
            in the heap

"""


from heapq import *

# Using built in functions
def find_k_largest_numbers(nums, k):
    result = []
    # TODO: Write your code here
    heapify(nums)

    return nlargest(k, nums)


# Actually finding the n largest using a min heap
def find_k_largest_numbers(nums, k):
    result = []
    # TODO: Write your code here
    if len(nums) <= k:
        return nums

    for i in range(k):
        heappush(result, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > result[0]:
            heappop(result)
            heappush(result, nums[i])

    return result

