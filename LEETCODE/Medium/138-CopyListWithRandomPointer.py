"""
Leetcode: 138. Copy List with Random Pointer

Attempts: 1
Completed: Y
Acheived Ideal: Y

Time Complexity: O(2n)
Space Complexity: O(n) => Hashtable

Pattern: No real Pattern 
Technique: Use a hashtable to keep track of the corresponding copied nodes

Problems Encountered:
Other Solutions:

"""


"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None: 
            return None 
        current = head
        copyHead,copyCurrent = None, None
        newRefTable = {None: None}
        
        # Create the LL copy without randoms 
        while current:
            copyNode = Node(current.val)
            newRefTable[current] = copyNode
            if copyHead == None:
                copyHead, copyCurrent = copyNode, copyNode
            else:
                copyCurrent.next = copyNode
                copyCurrent = copyCurrent.next 
            
            current = current.next
            
        current = head 
        
        while current:
            copiedNode = newRefTable[current]
            copiedNodeRandom = newRefTable[current.random]
            copiedNode.random = copiedNodeRandom
            current = current.next
        
        return copyHead
        
        
        
        
        
        
        
        
                
        
        