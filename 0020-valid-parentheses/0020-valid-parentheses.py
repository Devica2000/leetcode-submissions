class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {']':'[', '}':'{', ')':'('}
        stack = []

        for c in s:
            #if paranthesis is a key in the dict mapping
            if c in mapping:
                #make sure the stack is NOT empty
                #the stack cannot start with a close paranthesis
                #the last element is the matching value
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        #can be condensed into 1 line
        #return True if not stack else False        
        if not stack:
            return True
        else:
            return False












        valid = {')' : '(', '}' : '{', ']': '['}
        stack = []
        for c in s:
            if c in valid:
                # if it is a closing parantheses
                # then we need to make sure that
                # stack is not empty and the 
                # value at top of stack is a valid
                # opening parantheses
                if stack and stack[-1] == valid[c]:
                    stack.pop()
                # if we get an open parantheses
                else:
                    return False
            else:
                stack.append(c)
        # only return true if stack is not empty
        # since all pairs would have matched        
        return True if not stack else False

