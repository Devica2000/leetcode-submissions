class MinStack:

    def __init__(self):
        #initializing the two stacks
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        #use built in function to add element to the main stack
        self.stack.append(val)
        #append to minstack if it is empty
        #otherwise append the min value of val, top of stack
        # if self.minStack:
        #     val = min(val, self.minStack[-1])
        #     self.minStack.append(val)
        # else:
        #     self.minStack.append(val)
        #can be condensed into a single line in python
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()