# Leetcode: 75. Sort Colors

# Attempts:1
# Completed: Y
# Acheived Ideal: N

# Time Complexity: O(n)
# Space Complexity:

# Solving process: Two pass
# Problems Encountered:

# Other Solutions: Dutch Partition


# Two Pass
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        i = 0
        while zeros > 0:
            nums[i] = 0
            zeros -= 1
            i += 1
        while ones > 0:
            nums[i] = 1
            ones -= 1
            i += 1
        while twos > 0:
            nums[i] = 2
            twos -= 1
            i += 1

        return nums

# Dutch Partitioning One pass O(2n)


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:  # white pointer is on a red
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

        return nums
