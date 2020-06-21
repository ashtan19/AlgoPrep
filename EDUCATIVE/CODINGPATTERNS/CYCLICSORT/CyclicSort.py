'''
Question: Cyclic Sort

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Cyclic Sort
Technique: Check if index and value match. If not, swap. 


'''


def cyclic_sort(nums):
    # TODO: Write your code here
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] == nums[j]:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
    return nums
