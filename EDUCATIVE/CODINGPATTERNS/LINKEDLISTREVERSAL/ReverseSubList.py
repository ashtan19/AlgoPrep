
'''
Question: Reverse Sub List of LL

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: LL Reversal 
Technique: 


'''


def reverse_sub_list(head, p, q):
    # TODO: Write your code here
    if p == q:
        return head
    reverse_start = head
    # Find the node before P
    while reverse_start.next.value != p and reverse_start.next != None:
        reverse_start = reverse_start.next
    reverse_current, reverse_end = reverse_start.next, reverse_start.next

    while reverse_current.value != q:
        reverse_next = reverse_current.next
        reverse_current.next = reverse_start.next
        reverse_start.next = reverse_current
        reverse_current = reverse_next

    # One more iteration for q
    reverse_next = reverse_current.next
    reverse_current.next = reverse_start.next
    reverse_start.next = reverse_current
    reverse_end.next = reverse_next

    return head
