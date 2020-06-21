'''
Question: Find Duplicate Number

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Cyclic Sort
Technique: Cyclic Sort. Can also use fast and slow pointer


'''


def find_duplicate(nums):
    # TODO: Write your code here
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i:
            return nums[i]
    return -1
