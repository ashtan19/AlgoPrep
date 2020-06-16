# Leetcode: 56. Merge Intervals

# Attempts: 1
# Completed: Y
# Acheived Ideal: Y

# Time Complexity: O(n)
# Space Complexity: O(n)

# Solving process:
# Problems Encountered:

# Other Solutions:



'''
Input: Given a list of intervals -> List of lists that have 2 elements 
Output: Want to return a list of intervals ->list  of lists 
        Its <= len of original list

Sample: 
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Questions:
1) Is our input sorted in anyway? if it is, it would be easier 
2) are there reverse intervals? 

Three cases: 
1) when item is outside of range -> just append to result
2) when item overlaps previous range -> merge
3) when item is inside of range -> dont add 


Solving Process:
1) Need to sort the list based on the first element
2) Result = [interval[0]]
3) For interval in intervals in range 1 - end
    -> check if iterval[0] is > result[curindex][1]:
            then append iterval to result
    -> else check if iterval[0] <= result[curindex][1] and iterval[1] >=result[curindex][1]:
    result[curindex][1] = iterval[1]
    -> all other cases, do not add the interval 
4) return result
    


edge cases: 
negative numbers 

'''


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return intervals
        intervals = sorted(intervals, key=itemgetter(0))
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start > result[-1][1]:
                result.append(intervals[i])
            elif start <= result[-1][1] and end > result[-1][1]:
                result[-1][1] = end
        return result
