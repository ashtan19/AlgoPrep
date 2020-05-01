# CTCI: 3.5 Sort stack with only one temp stack 

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solving process:
# Problems Encountered: 

class Stack: 
    def __init__(self) :
        self.data = []
        self.min = 10000000000
        
    def push(self, value):
        self.data.append(value)
        if (value < self.min):
            self.min = value
    
    def pop(self):
        value = self.data.pop()
        # if (value == self.min):
        #     self.min = min(self.data)
        return value

    def peek(self):
        return self.data[-1] # Return last element

    def isEmpty(self):
        if self.data == []:
            return True
        else: return False
    
    def smallest(self):
        return self.min

def sortStack (inputStack ):
    if inputStack == None : return None
    if inputStack.isEmpty(): return inputStack

    tempStack = Stack()
    tempVar = None

    while (not inputStack.isEmpty()):
        tempVar = inputStack.pop()
        while (not tempStack.isEmpty() and tempVar < tempStack.peek()):
            inputStack.push(tempStack.pop())
        tempStack.push(tempVar)
    
    while (not tempStack.isEmpty()):
        inputStack.push(tempStack.pop())
    
    return inputStack


testStack = Stack()
testStack.push(0)
testStack.push(3)
testStack.push(1)
testStack.push(2)
testStack.push(7)
testStack.push(6)
testStack.push(10)

print(testStack.data)

testStack2 = sortStack(testStack)
print(testStack2.data)