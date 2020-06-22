'''
Question: Reverse Every K Elements in LL

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: LL Reversal
Technique: 


'''


def reverse_every_k_elements(head, k):
    # TODO: Write your code here
    if k < 2 or head.next == None:
        return head
    pre_head = Node(1)
    pre_head.next = head
    i = 0
    reverse_start, reverse_current, reverse_end = pre_head, head, head
    # For the very first time, we need to assign head
    while i < k and reverse_current:
        reverse_next = reverse_current.next
        reverse_current.next = reverse_start.next
        reverse_start.next = reverse_current
        reverse_current = reverse_next
        i += 1
    head = reverse_start.next

    while reverse_current:

        reverse_start = reverse_end
        reverse_end = reverse_current
        i = 0

        while i < k and reverse_current:
            reverse_next = reverse_current.next
            reverse_current.next = reverse_start.next
            reverse_start.next = reverse_current
            reverse_current = reverse_next
            i += 1
    reverse_end.next = None
    return head

# Clean Solution


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        # after reversing the LinkedList 'current' will become the last node of the sub-list
        last_node_of_sub_list = current
        next = None  # will be used to temporarily store the next node
        i = 0
        while current is not None and i < k:  # reverse 'k' nodes
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # connect with the previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        # connect with the next part
        last_node_of_sub_list.next = current

        if current is None:
            break
        previous = last_node_of_sub_list
    return head
