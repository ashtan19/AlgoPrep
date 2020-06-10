# Leetcode: 240. Search a 2D Matrix II

# Attempts: 1
# Completed: Y
# Acheived Ideal: Y

# Time Complexity: O(m+n)
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions: O(m+n) search


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]] or matrix == None:
            return False
        lenarr = len(matrix[0])
        for arr in matrix:
            if arr[0] <= target and arr[-1] >= target:
                if self.binarySearch(arr, 0, lenarr-1, target) == True:
                    return True

        return False

    def binarySearch(self, arr, l, r, x):
        while l <= r:
            mid = l + (r-l) // 2

            if arr[mid] == x:
                return True
            elif arr[mid] < x:
                l = mid+1
            else:
                r = mid - 1

        return False

# Because of the problem description, we can also do it in m+n time


class Solution(object):
    def searchMatrix(self, matrix, target):
        j = -1
        for row in matrix:
            while j + len(row) >= 0 and row[j] > target:
                j -= 1
            if j + len(row) >= 0 and row[j] == target:
                return True
        return False
