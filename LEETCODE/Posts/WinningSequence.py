"""
Leetcode: Amazon OA Winning Sequence
Link: https://leetcode.com/discuss/interview-question/907575/

Attempts: 1
Completed: N, but got it conceptually 
Acheived Ideal:
Under 30 Mins: 

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Array
Technique: Check if upper - lower + 1 can fit in num-1 then generate the descending sequence and 
            then add the ascending sequence. Can use a Deque to accelerate the ascending insertion

Problems Encountered: Missed the edge case where , range is not big enough to fit in num 
Other Solutions:



Question: 
Position: Intern
Platform: SHL
Location: US
Date: Oct 2020

A challenge in an Amazon Hackathon programming competition requires the construction of a sequence using a specified number of integers within a range. The sequence must be strictly increasing at first and then strictly decreasing. The goal is to maximize the sequence array elements starting from the beginning. For example, [4, 5, 4, 3, 2] beats [3,4,5,4,3] because its first element is larger, and [4, 5, 6, 5, 4] beats [4,5,4,3,2] because its third element is larger. Given the length of the sequence and the range of integers, return the winning sequence. If it is not possible to construct such a sequence, return -1.
Write an algorithm that returns a winning sequence and -1 if the sequence is not possible.

Input
The input to the function/method consists of three arguments: num, an integer representing the size of sequence to create; lowerEnd, an integer representing the lower end of integer range; upperEnd, an integer representing the upper end of integer range.

Output
Return a list of integers representing the winning sequence and if the sequence is not possible then return a list with an integer -1.

Constraints
3 <= num <= 10^5
1 <= lowerEnds <= upperEnds <= 10^5

Example
Input:
num = 5
lowerEnd = 3
upperEnd = 10

Output:
[9,10,9,8,7]

Explanation:
In this case, [9, 10, 9, 8, 7] is the winning sequence. It maintains the constraints of being first strictly increasing and then strictly decreasing, and there is no way to have integers in the sequence that are greater than [9, 10, 9, 8, 7].
So the output is [9, 10, 9, 8, 7].
"""


def sequence(n, upperBound, lowerBound):
    nums = (upperBound - lowerBound) * 2 + 1
    if nums < n:
        return [-1]
    ans = []
    for i in range(min(upperBound - lowerBound + 1, n - 1)):
        ans.append(upperBound - i)
    for i in range(n - len(ans)):
        ans.insert(0, upperBound - i - 1)
    return ans


print(sequence(5, 10, 3), "should be [9,10,9,8,7]")
print(sequence(5, 10, 8), "should be [8, 9, 10, 9, 8]")
print(sequence(5, 9, 10), "should be [-1]")
print(sequence(4, 6, 3), "should be [5, 6, 5, 4]")
print(sequence(10, 30, 20),
      "should be [29, 30, 29, 28, 27, 26, 25, 24, 23, 22]")
print(sequence(3, 8, 7), "should be [7, 8, 7]")
print(sequence(10, 10, 3), "should be [8, 9, 10, 9, 8, 7, 6, 5, 4, 3]")
