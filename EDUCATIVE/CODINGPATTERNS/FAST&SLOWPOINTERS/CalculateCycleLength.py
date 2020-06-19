'''
Question: 

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Fast and Slow Pointer
Technique: 


'''


def has_cycle(head):
    # TODO: Write your code here
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return calculate_cycle_length(slow)
    return False


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length
