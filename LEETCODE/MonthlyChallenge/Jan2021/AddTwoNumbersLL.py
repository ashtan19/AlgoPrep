"""
Leetcode: 2. Add Two Numbers

Attempts:1
Completed:Y
Acheived Ideal: Max(m,n)
Under 30 Mins: N

Time Complexity: Max(m,n)
Space Complexity: 1 b/c reusing L1 and L2 nodes 

Pattern: Linked List    
Technique: Iterating through both lists

Problems Encountered: Tricky pointer situation 
Other Solutions:

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        p1, p2 = l1, l2
        carry = 0

        s = p1.val + p2.val
        if s > 9:
            carry = 1
            s %= 10
        p1.val = s

        while p1.next or p2.next:
            if not p1.next and p2.next:
                p1.next = p2.next
                p2.next = None

            num1 = p1.next.val
            num2 = p2.next.val if p2.next else 0

            p1 = p1.next
            p2 = p2.next if p2.next else p2

            s = num1 + num2 + carry
            carry = 0
            if s > 9:
                carry = 1
                s %= 10
            p1.val = s

        if carry == 1:
            last_node = ListNode(1, None)
            p1.next = last_node

        return l1
