# Leetcode: 21 Merge two sorted lists

# Attempts: 2

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered:

# Other Solutions:


# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

# recursively


def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

# in-place, iteratively


def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


# Attempt 2

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newlisthead = ListNode()
        newlistiterator = newlisthead
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    newlistiterator.next = l1
                    l1 = l1.next
                    newlistiterator = newlistiterator.next
                else:
                    newlistiterator.next = l2
                    l2 = l2.next
                    newlistiterator = newlistiterator.next

            elif l1 and not l2:
                newlistiterator.next = l1
                break
            elif l2 and not l1:
                newlistiterator.next = l2
                break
        return newlisthead.next
