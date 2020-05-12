# Leetcode: 141 Linked List Cycle

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
