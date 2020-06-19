'''
Question: 

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Fast and Slow Pointers
Technique: Fast moves at 2x speed 


'''


def has_cycle(head):
    # TODO: Write your code here
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
