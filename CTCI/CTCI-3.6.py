# CTCI: 3.6 Animal Shelter Stack

# Time Complexity: enqueue O(n), DequeueAny O(1), dequeue O(n) if animal you are looking for is the youngest.
# Space Complexity: O(n)
# Solving process:
# Problems Encountered: Linked list Implementation had problems

# Other Solutions: Instead of using the 3 queues, you could use two queues with timestamps. then when you wanna dequeueany, peek both


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
        if index >= self.length():
            print ("Out of range")
            return None
        cur_index = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_index == index : return cur.data
            cur_index += 1
    
    def erase(self,index):
        if index >= self.length():
            print ("Out of range")
            return None
        cur_index = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_index == index: 
                last_node.next = cur.next 
                return
            cur_index +=1
        
class AnimalShelter:
    def __init__(self):
        self.shelterList = linked_list()
        self.dogList = linked_list()
        self.catList = linked_list()
        self.count = 0
    
    def enqueue( self, animal ):
        self.shelterList.append((animal, self.count))
        if animal == "dog" : 
            self.dogList.append(self.count)
        elif animal == "cat" :
            self.catList.append(self.count)
        else: 
            print("Sorry, we only accept Dogs and Cats")
        self.count += 1
    
    def dequeueAny(self):
        animal, animalNum = self.shelterList.get(0)
        self.shelterList.erase(0)
        if animal == "dog" : 
            self.dogList.erase(0)
        else:
            self.catList.erase(0) 

    def dequeueDog(self):
        animalNum = self.dogList.get(0)
        print(animalNum)

        #Find the count of the oldest dog
        iter = 0
        cur = self.shelterList.head
        while True:
            cur = cur.next
            if cur.data == ("dog", animalNum) :
                print(iter)
                self.shelterList.erase(iter)
                self.dogList.erase(0)
                return
            iter += 1
        

    def dequeueCat(self):
        animalNum = self.catList.get(0)

        #Find the count of the oldest dog
        iter = 0
        cur = self.shelterList.head
        while True:
            cur = cur.next
            if cur.data == ("cat", animalNum) : 
                 break
            iter += 1
        
        self.shelterList.erase(iter)
        self.catList.erase(0)



#Test for the [ dog, dog, cat, cat ] and take out dog (which would be the first dog of count 0) 
testShelter = AnimalShelter()
testShelter.enqueue("dog")
testShelter.enqueue("dog")
testShelter.enqueue("cat")
testShelter.enqueue("cat")

testShelter.shelterList.display()
testShelter.dogList.display()
testShelter.catList.display()

testShelter.dequeueDog()
testShelter.shelterList.display()
testShelter.dogList.display()
testShelter.catList.display()

#Test [dog, dog , cat , cat] and take out cat. Dog stays intack 
testShelter.dequeueCat()
testShelter.shelterList.display()
testShelter.dogList.display()
testShelter.catList.display()

#Test [dog, dog, cat , cat] and take out any => dog should return 
testShelter.dequeueAny()
testShelter.shelterList.display()
testShelter.dogList.display()
testShelter.catList.display()

#Test enqueuing animal that is not dog or cat
testShelter.enqueue("whale")

