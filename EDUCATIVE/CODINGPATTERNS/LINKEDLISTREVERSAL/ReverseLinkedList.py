'''
Question: Reverse LL

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: In-Place LL Reversal
Technique: 


'''


def reverse(head):
    # TODO: Write your code here
    pointer = head
    head = None
    while pointer != None:
        cur_node = pointer.next
        pointer.next = head
        head = pointer
        pointer = cur_node
    return head
