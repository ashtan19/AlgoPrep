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
        prev_start, prev_end = intervals[i-1]
        cur_start, cur_end = intervals[i]
        if cur_start < prev_end:
            return False
    return True
