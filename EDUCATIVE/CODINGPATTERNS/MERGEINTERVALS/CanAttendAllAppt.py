'''
Question: Conflicting Appointments (medium)

Time Complexity: O(nlogn)
Space Complexity: O(n)

Pattern: Merge Intervals 
Technique: Sort Intervals by start, Check if start is before previous end


'''


def can_attend_all_appointments(intervals):
    # TODO: Write your code here
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True
