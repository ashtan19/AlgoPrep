'''
Question: Insert Interval

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Merge Intervals
Technique: 


'''


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
