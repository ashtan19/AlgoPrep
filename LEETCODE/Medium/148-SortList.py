# Leetcode: 148. Sort List

# Attempts: 1
# Completed: Y
# Acheived Ideal: N

# Time Complexity: O(n^2)
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions:



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        newhead = head
        pointer = head.next
        newhead.next = None
        while pointer != None:
            next = pointer.next
            if pointer.val < newhead.val:
                pointer.next = newhead
                newhead = pointer
            else:
                newheadpointer = newhead
                while newheadpointer.next != None and newheadpointer.next.val < pointer.val:
                    newheadpointer = newheadpointer.next
                newheadpointernext = newheadpointer.next
                newheadpointer.next = pointer
                pointer.next = newheadpointernext
            pointer = next
        return newhead
