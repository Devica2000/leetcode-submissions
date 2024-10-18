class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #O(n)

        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                #we need to maintain the order in 
                #which the elements were added to the stack
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                #use int to convert to an integer
                #and round to 0 at the same time
                stack.append(int(b/a))
            else:
                #we need to convert characters to interger
                #before performing operations
                stack.append(int(c))
        
        return stack[0]














        #use a stack
        #reading from L to R
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                # to round to 0, we use int
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]

        