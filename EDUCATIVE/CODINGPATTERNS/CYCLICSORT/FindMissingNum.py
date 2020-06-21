'''
Question: Find the Missing Number (easy)

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Cyclic Sort
Technique: Cyclic Sort but keep in the mind the numbers that go out of bounds of the array
            and skip them. When you skip them, the spot that is skipped will the replaced 
            if its index in in the array. Else, it the number that is missing.


'''


def find_missing_number(nums):
    # TODO: Write your code here
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return n
