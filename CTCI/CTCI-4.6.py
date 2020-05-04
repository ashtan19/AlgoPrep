# CTCI: 4.6 BST Successor

# Time Complexity: O(logn)
# Space Complexity: O(1)
# Solving process: Draw out a BST and check scenarios of how to find next successor
# Problems Encountered: 

# Other Solutions:

class TreeNode:
    def __init__(self, x, parent):
        self.val = x
        self.left = None
        self.right = None
        self.parent = parent


def inOrderSuccessor (currentNode):
    if not currentNode.right: 
        parentnode = currentNode.parent
        if currentNode == parentnode.left:
            return currentNode.parent
        else: 
            while currentNode != parentnode.left:
                currentNode = parentnode
                parentnode = currentNode.parent
                if parentnode == None:
                    print("No successor")
                    return None
            return parentnode
    else: 
        nextNode = currentNode.right
        while nextNode.left != None :
            nextNode = nextNode.left
        return nextNode


testTree = TreeNode(4,None)
testTree.left = TreeNode(2, testTree)
testTree.left.left = TreeNode(1, testTree.left)
testTree.left.right = TreeNode(3, testTree.left)

testTree.right = TreeNode(6, testTree)
testTree.right.left = TreeNode(5, testTree.right)
testTree.right.right = TreeNode(7, testTree.right)

testLeftChildLeaf = inOrderSuccessor(testTree.left.left) # Should return 2
print(testLeftChildLeaf.val)

testRightChildLeaf = inOrderSuccessor(testTree.left.right) #Should return 4
print(testRightChildLeaf.val)

testParentwithRightChildLeaf = inOrderSuccessor(testTree.left) #should return 5
print(testParentwithRightChildLeaf.val)

testParentwithRightChild = inOrderSuccessor(testTree) #should return 3
print(testParentwithRightChild.val)

testEndNode = inOrderSuccessor(testTree.right.right)
print(testEndNode.val)




