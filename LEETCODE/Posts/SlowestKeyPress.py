"""
Leetcode: Amazon Slowest Key Press

Attempts: 1
Completed: N but got it conceptually
Acheived Ideal:
Under 30 Mins:

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Iteration
Technique:

Problems Encountered:
Other Solutions:

"""

# Time-Complexity: O(n)
# Space-Complexity: O(1)


def slowestKey(keyTimes):
	slowestPos = 0
	slowestTime = keyTimes[0][1]
	for i in range(1, len(keyTimes)):
		currTime = keyTimes[i][1] - keyTimes[i-1][1]
		if currTime > slowestTime:
			slowestPos = i
			slowestTime = currTime
    return chr(97 + keyTimes[slowestPos][0])
	
print(slowestKey([[0,2],[1,5],[0,9],[2,15]]))
