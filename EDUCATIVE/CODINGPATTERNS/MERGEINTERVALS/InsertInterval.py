'''
Question: Insert Interval

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Merge Intervals
Technique: If Intervals are already sorted, just figure out when to consider the new interval


'''

# O(nlogn) b/c of the sort


def insert(intervals, new_interval):

    # TODO: Write your code here
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        merged_start, merged_end = merged[-1]
        if start > merged_end:
            merged.append(intervals[i])
        else:
            if end > merged_end:
                merged[-1][1] = end

    return merged

# O(n)


def insert(intervals, new_interval):
    merged = []
    i, start, end = 0, 0, 1

    # skip (and add to output) all intervals that come before the 'new_interval'
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    # merge all intervals that overlap with 'new_interval'
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    # insert the new_interval
    merged.append(new_interval)

    # add all the remaining intervals to the output
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged
