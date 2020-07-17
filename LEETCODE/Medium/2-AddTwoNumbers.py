"""
Leetcode: 2. Add Two Numbers

Attempts: 1
Completed: Y
Acheived Ideal: N

Time Complexity: O(n) => Longest List
Space Complexity: O(1)

Pattern: Two pointers
Technique: Have a while loop that adds and carries value over 

Problems Encountered: Missed many edge cases. eg, when one number is 9999 => need to continue the carryValue
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
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        cur1, cur2 = l1, l2
        prev2 = None
        carryOver = 0

        while cur1 or cur2:
            cur1Val = cur1.val if cur1 else 0
            cur2Val = cur2.val if cur2 else 0
            digitSum = cur1Val + cur2Val + carryOver
            carryOver = 0
            if digitSum > 9:
                digitSum %= 10
                carryOver = 1
            print(digitSum)
            if cur2.next == None and cur1:
                cur1.next, cur2.next = cur2.next, cur1.next
            cur2.val = digitSum
            prev2 = cur2
            cur1 = cur1.next if cur1 else cur1
            cur2 = cur2.next if cur2 else cur1

        if carryOver == 1:
            prev2.next = ListNode(carryOver)

        return l2


def addTwoNumbers(self, l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10
    return dummy.next

