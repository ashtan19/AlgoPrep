'''
Question: 

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Fast and slow pointers
Technique: 


'''


def find_middle_of_linked_list(head):
    # TODO: Write your code here
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
