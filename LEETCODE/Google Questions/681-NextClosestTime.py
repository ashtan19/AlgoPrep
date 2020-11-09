"""
Leetcode: 681 Next Closest Time

Attempts:1
Completed: y
Acheived Ideal: Y
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(1) b/c only need extra array of size 4

Pattern: Combinatorics
Technique: Check each position for the next best number else set it to the smallest digit and check the next position

Problems Encountered:
Other Solutions: Can use python built in combinatorics 

"""


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time_list = list(time)
        print(time_list)
        nums = [time[0], time[1], time[3], time[4]]
        nums.sort()

        def find_bigger(nums, time_list, index, limit):
            for num in nums:
                if num > time_list[index] and num <= limit:
                    time_list[index] = num
                    return True
            time_list[index] = nums[0]
            return False

        if find_bigger(nums, time_list, 4, '9'):
            return ''.join(time_list)

        if find_bigger(nums, time_list, 3, '5'):
            return ''.join(time_list)

        if time_list[0] == '2':
            if find_bigger(nums, time_list, 1, '4'):
                return ''.join(time_list)
            else:
                time_list[0] = nums[0]
                return ''.join(time_list)
        else:
            if find_bigger(nums, time_list, 1, '9'):
                return ''.join(time_list)
            else:
                time_list[0] = nums[0]
                return ''.join(time_list)


class Solution(object):
    def nextClosestTime(self, time):
        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        allowed = {int(x) for x in time if x != ':'}
        for h1, h2, m1, m2 in itertools.product(allowed, repeat=4):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                cand_elapsed = (cur - start) % (24 * 60)
                if 0 < cand_elapsed < elapsed:
                    ans = cur
                    elapsed = cand_elapsed

        return "{:02d}:{:02d}".format(*divmod(ans, 60))
