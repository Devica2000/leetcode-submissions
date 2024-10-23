class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Only add open brackets if openN < n
        #only add closing bracket is closeN < openN
        #Valid IFF openN == closeN == n

        stack = []
        res = []

        def backtracking(openN, closeN):
            if openN == closeN == n:
                #join all elements in stack to string
                res.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closeN)
                stack. pop()

            if closeN < openN:
                stack.append(")")
                backtracking(openN, closeN + 1)
                stack.pop()

        backtracking(0,0)
        return res

        #use backtracking

        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0,0)
        return res