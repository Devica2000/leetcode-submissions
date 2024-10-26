class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #make an array of pairs of position, speed
        #use list comprehension
        pair = [[p,s] for p, s in zip(position, speed)]
        stack = []

        #sort the pair array by position
        #we go from right to left
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)














        pair = [[p,s] for p,s in zip(position,speed)]
        # to return the number of car fleet at the end
        stack = []

        # iterate in reverse sorted order 
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p)/s)
            #check if stack is non empty and there are at least 2 elements
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)