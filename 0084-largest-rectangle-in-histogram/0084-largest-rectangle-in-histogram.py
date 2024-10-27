class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair : (index, height)

        for i,h in enumerate(heights):
            #index of current height
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                #extend index backward to the index we saw
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea











        # O(n) time and space complexity
        # use a stack to keep track of the index, height pair

        maxArea = 0
        stack = []

        for i,h in enumerate(heights):
            #before putting anything in the stack
            #initialize start as the current index value
            #since we do not know it could be extended backwards
            start = i

            #check if the stack is not empty and
            #if height top value > current value

            while stack and stack[-1][1] > h:
                #if true, I want to pop the top element
                #retrive the index and height
                #to compute maxArea
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                #now since we popped elements
                #we can give the current element a backward index
                start = index
            stack.append((start, h))      

        #loop to compute the area of the elements left in the stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

