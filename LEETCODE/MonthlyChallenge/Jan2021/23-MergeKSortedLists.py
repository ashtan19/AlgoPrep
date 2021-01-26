"""
Leetcode: 23. Merge k Sorted Lists

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(nlogk) where k = #lists, n = total nodes
Space Complexity: O(k)

Pattern: Merge k 
Technique: Use a heap to find the min head of each list

Problems Encountered:
Other Solutions: Merge with Divide And Conquer

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq

        temp_node = ListNode()
        result = temp_node

        heap = []

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        while heap:
            v, s_node = heapq.heappop(heap)
            temp_node.next = s_node
            temp_node = temp_node.next
            if s_node.next != None:
                heapq.heappush(heap, (s_node.next.val, s_node.next))

        return result.next


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
