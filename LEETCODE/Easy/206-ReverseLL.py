# Leetcode: 206 Reverse LL

# Attempts: 2

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered:

# Other Solutions: Can do recursively


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        cur = head
        while cur != None:
            temp = cur
            cur = cur.next
            temp.next = reverse
            reverse = temp
        return reverse


# Attempt 2
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = None
        while head:
            pointer = head
            head = head.next
            pointer.next = newhead
            newhead = pointer

        return newhead
