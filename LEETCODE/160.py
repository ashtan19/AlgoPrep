# Leetcode: 160 LL Intersection

# Time Complexity: O(n), O(n)
# Space Complexity: O(n), O(1)
# Solving process:
# Problems Encountered:

# Other Solutions: The two pointer solution where when you pointers reach the end of their list, point to head of other list
# the pointers will then meet at the intersection in that iteration


# Hash Table Solution
class Solution(object):
    def getIntersectionNode(self, head1, head2):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        hashlist1 = {}
        hashlist2 = {}

        while head1 != None or head2 != None:
            if head1 != None:
                hashlist1[head1] = None  # Just need the key
                if head1 in hashlist2:
                    return head1
                head1 = head1.next
            if head2 != None:
                hashlist2[head2] = None
                if head2 in hashlist1:
                    return head2
                head2 = head2.next
        return None


# Two Pointer Solution
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA  # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None

# the idea is if you switch head, the possible difference between length would be countered.
# On the second traversal, they either hit or miss.
# if they meet, pa or pb would be the node we are looking for,
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
