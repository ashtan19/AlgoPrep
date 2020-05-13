# Leetcode: 234 Palindrome LL

# Time Complexity: O(n)
# Space Complexity: O(n) O(1)
# Solving process:
# Problems Encountered:

# Other Solutions: Two Pointer Method: Find the middle point and reverse the second half then compare with start of list


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        p1 = head.next
        p2 = ListNode(head.val)

        while p1 != None:
            newnode = ListNode(p1.val, p2)
            p2 = newnode
            p1 = p1.next

        while head != None:
            if head.val != p2.val:
                return False
            head = head.next
            p2 = p2.next

        return True


# Two Pointer
def isPalindrome(self, head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node:  # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True
