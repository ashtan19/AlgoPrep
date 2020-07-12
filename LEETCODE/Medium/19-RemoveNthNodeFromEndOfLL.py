"""
Leetcode: 19. Remove Nth Node From End of List

Attempts: 1
Completed: Y but missed edgecase 
Acheived Ideal: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Two Pointer
Technique: Have a counter that increments, when counter reaches, start a new pointer that will iterate - return that pointer

Problems Encountered: Missed the edge case where you are deleting the first node - there is no node before first node
Other Solutions: Could also have a dummy head that you put in front of head - dont have to take care of edgecase but extra space

"""


#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None or n == 0:
            return head
        current, beforeNth = head, None
        count = 0
        while current:
            if count == n:
                beforeNth = head
            elif count > n:
                beforeNth = beforeNth.next
            count += 1
            current = current.next

        # This case if when there is only one element and the beforeNth will not be set
        if beforeNth == None:
            return head.next

        beforeNth.next = beforeNth.next.next

        return head
