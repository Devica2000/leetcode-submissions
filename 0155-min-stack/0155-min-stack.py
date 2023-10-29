class MinStack:

    def __init__(self):
        #defining two stack using array
        # a main stack and a min stack
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # we need to keep the min(value in minstack, val) in the minstack
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        # function only called when the stack is non empty
        return self.stack[-1]

    def getMin(self) -> int:
        # function only called when the stack is non empty
        return self.minstack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()