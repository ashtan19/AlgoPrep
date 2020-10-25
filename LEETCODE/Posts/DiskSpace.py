"""
Leetcode: Amazon OA Max Disk Space

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(n*segmentLength) but can be O(n)
Space Complexity: O(1) but can be O(segmentlength)

Pattern: Sliding window
Technique: Brute Force or Use a deque to keep track of min value index

Problems Encountered:
Other Solutions:

"""


from collections import deque

# O(n * segmentLength) time , O(1) space


def maxDiskSpace(numComputer, hardDiskSpace, segmentLength):
    if segmentLength == 0:
        return 0
    max_space = 0
    for i in range(0, numComputer-segmentLength + 1):
        min_space = float("inf")
        for j in range(segmentLength):
            min_space = min(min_space, hardDiskSpace[i+j])
        max_space = max(max_space, min_space)

    return max_space


print(maxDiskSpace(3, [8, 2, 4], 2))

'''
Idea:
    - Have a queue for sliding window
    - When you see a new element, check if the current element is smaller than anything on the right side of the queue
    - If it is, keep popping elements off until you find a smaller element or deque is empty
    - at every iteration, check the left side of the queue to get the min value 
    - pop the left deque >= segmentlength
'''

# O(n) time b/c for every element, we are only insert, popping and iterating over once each
# O(segmentlength) for deque


def maxDiskSpaceII(numComputer, hardDiskSpace, segmentLength):
    dqueue = deque()
    max_space = 0

    for i in range(numComputer):
        disk_space = hardDiskSpace[i]
        if dqueue and dqueue[0] < i-segmentLength+1:
            dqueue.popleft()

        while dqueue and hardDiskSpace[dqueue[-1]] >= disk_space:
            dqueue.pop()
        dqueue.append(i)
        if i > segmentLength - 1:
            max_space = max(max_space, hardDiskSpace[dqueue[0]])

    return max_space


print(maxDiskSpaceII(6, [8, 2, 4, 5, 6, 1], 2))
