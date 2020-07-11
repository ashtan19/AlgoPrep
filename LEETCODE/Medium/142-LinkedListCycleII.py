"""
Leetcode: 142 Linked List Cycle II

Attempts: 1
Completed: Y
Acheived Ideal: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Fast and Slow Pointer
Technique: When pointers meet, have one of the pointers start from head again and when they meet again, its the start of the cycle

Problems Encountered: None
Other Solutions: Hashmap but extra space

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next

                return fast

        return None
