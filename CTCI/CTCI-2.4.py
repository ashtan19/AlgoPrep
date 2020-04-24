# CTCI 2.4 Linked List Partition


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


# def partition(llist , divider):
#     thenode = llist.head.next

#     head = thenode
#     tail = thenode

#     while thenode != None:
#         next = thenode.next
#         if thenode.data < divider:
#             thenode.next = head
#             head = thenode
#         else:
#             tail.next = thenode
#             tail = thenode
#         node = next

#     tail.next = None 

#     llist.head = head

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
    

    # if llist.head == None: return llist
    # if llist.head.next == None: return llist

    # runner = llist.head.next
    # left = llist.head

    # while (runner.next is not None):
    #     if runner.next.data >= divider: runner.next = runner.next.next
    #     else: 
    #         llist.head = runner.next
    #         runner.next = runner.next.next
    #         llist.head.next = left
    #         runner = runner.next
    

test_list = linked_list()
test_list.append(3)
test_list.append(5)
test_list.append(8)
test_list.append(10)
test_list.append(2)
test_list.append(1)
test_list.display()

partition(test_list, 5)
test_list.display()