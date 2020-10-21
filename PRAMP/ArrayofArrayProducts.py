'''
"""
Things I learned:
    - Check for corner cases before I start (missed case when there is only one element)
    - When Interviewer interrupted my train of thought, I was pretty affected, lost my pace, need to minimize
    - Need clearer communication 

"""



Question:
Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 20
[output] array.integer
'''

'''
arr =    [8, 10, 2]
result = [20, 16, 80]

left =  [1 , 8, 80]
right = [20 , 2, 1]

result = []

Idea: 
  - Create cumulative sums from left to right and another from right to left 
  - For each element, we take the cumulative sums from both sides and mutiply
  
  
left =  [1]

'''


def array_of_array_products(arr):
    if len(arr) == 1:
        return []

    left, right = [1], [1]
    result = []

    for i in range(0, len(arr)-1):
        left.append(arr[i] * left[i])
        right.append(arr[len(arr)-1-i] * right[i])

    for i in range(0, len(arr)):
        result.append(left[i] * right[len(arr)-i-1])

    return result


arr = [8, 10, 2]
print(array_of_array_products(arr))
