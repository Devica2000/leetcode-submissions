class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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

        