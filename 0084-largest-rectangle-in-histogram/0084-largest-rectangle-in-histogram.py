class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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

