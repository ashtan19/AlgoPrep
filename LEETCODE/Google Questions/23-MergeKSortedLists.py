"""
Leetcode: 23. Merge k Sorted Lists

Attempts: 1
Completed: Y
Acheived Ideal: Y 
Under 30 Mins: Y

Time Complexity: O(nlogk)
Space Complexity: O(k)

Pattern: Linked List 
Technique: Heap

Problems Encountered:
Other Solutions:

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []

        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, lists[i]))

        result = ListNode()
        end = result
        while heap:
            node_val, node = heapq.heappop(heap)
            end.next = node
            end = end.next
            if node.next != None:
                heapq.heappush(heap, (node.next.val, node.next))

        return result.next


# Divide and Conquer Solution with in O(nlogk) time and O(1) space

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next
