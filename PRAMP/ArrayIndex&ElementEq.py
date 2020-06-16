# Attempts: 1
# Completed: Y
# Acheived Ideal: Y

# Time Complexity: O(logn)
# Space Complexity: O(1)

# Solving process: Binary Search or Brute Force(O(n))
# Problems Encountered:

# Other Solutions:


'''
Array Index & Element Equality
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[output] integer
'''

'''
Input: Sorted List of integers
Output: index where arr[index] == index 

Sample:
input: arr = [-8,0,2,5]
              0 ,1,2,3
             [-1,0,3,6]
              0 ,1,2,3
output: 2 # since arr[2] == 2

len(arr)/2 = m = 2
if 2

Binary Search: 
1) Take mid and check if arr[mid] == mid: 
    record min and go left 
2) arr[mid] > mid: 
    move right 
3) if  arr[mid] < mid:
    go left

Process: 
1) for loop to iterate arr
2) if arr[i] == i -> return i
2) outside for loop we return -1

[-1,0,3,6]
 0 ,1,2,3
 
 4
'''


def index_equals_value_search(arr):

    def binarySearch(left, right):
        minIndex = len(arr)
        while left <= right:
            mid = (right - left)/2 + left
            if arr[mid] < mid:
                left = mid + 1
            else:
                if arr[mid] == mid:
                    minIndex = mid
                right = mid - 1
        return minIndex

    result = binarySearch(0, len(arr)-1)
    if result == len(arr):
        return -1
    return result
