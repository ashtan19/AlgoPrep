'''
Question: Happy number

Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: fast and slow
Technique: 


'''


def find_happy_number(num):
    # TODO: Write your code here
    slow, fast = num, num
    while True:
        slow = find_sum(slow)
        fast = find_sum(find_sum(fast))
        if slow == fast:
            break
    return slow == 1


def find_sum(num):
    cur_sum = 0
    while num > 0:
        digit = num % 10
        cur_sum += digit * digit
        num //= 10
    return cur_sum
