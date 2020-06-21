'''
Question: Find Missing Nums

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Cyclic Sort
Technique: Similar to Cyclic Sort and Finding one number. But instead, you find more numbers
            place and add them into the array

'''


def find_missing_numbers(nums):
    missingNumbers = []
    # TODO: Write your code here
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i+1:
            missingNumbers.append(i+1)

    return missingNumbers
