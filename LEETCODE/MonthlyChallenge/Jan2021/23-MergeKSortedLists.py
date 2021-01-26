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
Other Solutions:

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
