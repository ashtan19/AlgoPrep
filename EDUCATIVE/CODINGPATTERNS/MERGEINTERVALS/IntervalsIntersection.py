'''
Question: Intervals Intersection

Time Complexity: O(n+m)
Space Complexity: O(n+m)

Pattern: Merge Intervals
Technique: Account for all cases of different interval intersections


'''


def merge(intervals_a, intervals_b):
    result = []
    cur_a, cur_b = 0, 0
    len_a = len(intervals_a)
    len_b = len(intervals_b)

    while cur_a < len_a and cur_b < len_b:
        start_a, end_a = intervals_a[cur_a]
        start_b, end_b = intervals_b[cur_b]
        if end_a < start_b:
            cur_a += 1
            continue
        elif start_a > end_b:
            cur_b += 1
            continue
        else:
            result.append([max(start_a, start_b), min(end_a, end_b)])
            if end_a < end_b:
                cur_a += 1
            else:
                cur_b += 1

    # TODO: Write your code here
    return result
