# CTCI: 2.6 Linked List Palindrome

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solving process: reverse the LL and then check if the LL are equal
# Problems Encountered: 

#Other Solutions: 1) Use a stack and a slow & fast runner in the LL, when fast reaches end of list, you start comparing stack to second half of the LL
# 2) Can do it recursively => get length of LL, Use length to get to middle of list. start passing back elements of the second half of the LL and check if the same

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = node()
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        
    def length(self) :
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        cur = self.head
        elements = []
        while cur.next != None:
            cur = cur.next 
            elements.append(cur.data)
        print(elements)
        
    def get(self, index):
        if index <= self.length():
            print ("Out of range")
            return None
        cur_index = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_index == index : return cur.data
            cur_index += 1
    
    def erase(self,index):
        if index <= self.length():
            print ("Out of range")
            return None
        cur_index = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_index == index: 
                last_node.next = cur.next 
            cur_index +=1


def LLisPal (inputLL ):
    if inputLL == None : return None
    tempList = None
    iterator = inputLL.next

    while iterator != None:
        # print(iterator.data)
        newNode = node(iterator.data)
        # print(newNode.data)
        newNode.next = tempList
        tempList = newNode
        # print(tempList.data)
        iterator = iterator.next

    inputIterator = inputLL.next
    tempIterator = tempList

    while inputIterator != None:
        # print(inputIterator.data)
        # print(tempIterator.data)
        if inputIterator.data != tempIterator.data:
            return False
        inputIterator = inputIterator.next
        tempIterator = tempIterator.next
    
    return True


test_list = linked_list()
test_list.append("g")
test_list.append("o")
test_list.append("n")
test_list.append("o")
test_list.append("g")
# test_list.append("z")
test_list.display()

print(LLisPal(test_list.head))