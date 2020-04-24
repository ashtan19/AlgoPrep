class Queue:
    def __init__(self):
        self.enqueueStack = []
        self.dequeueStack = []
    
    def reverseStack (self, stack1, stack2):
        i = 0
        while i < len(stack1):
            stack2.append(stack1.pop())
            i += 1
    
    def enqueue (self, value):
        if (len(self.dequeueStack) != 0): 
            i = 0 
            for i in range(len(self.dequeueStack)):
                self.enqueueStack.append(self.dequeueStack.pop())

        self.enqueueStack.append(value)
    
    def dequeue (self):
        if (len(self.enqueueStack) == 0):
            if (len(self.dequeueStack) == 0): # If trying to dequeue a empty queue, return None 
                return None
        else :
            for i in range(0,len(self.enqueueStack)):
                self.dequeueStack.append(self.enqueueStack.pop())
        
        return self.dequeueStack.pop()


myQueue = Queue()
print(myQueue.dequeue())
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
print(myQueue.enqueueStack)
print(myQueue.dequeue())
print(myQueue.enqueueStack)
print(myQueue.dequeueStack)

myQueue.enqueue(5)
print(myQueue.enqueueStack)
print(myQueue.dequeueStack)