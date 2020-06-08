# Leetcode: 141 Linked List Cycle

# Attempts : 2

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solving process:
# Problems Encountered:

# Other Solutions: Can also use fast and slow pointer

# HashSet


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodesSeen = {}
        while head != None:
            if head in nodesSeen:
                return True
            else:
                nodesSeen[head] = None
            head = head.next

        return False

# Attempt 2


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = head
        slow = head

        while fast and fast.next and fast.next.next and slow and slow.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
