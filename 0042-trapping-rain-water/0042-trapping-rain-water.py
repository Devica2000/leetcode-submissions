class Solution:
    def trap(self, height: List[int]) -> int:

        #Two Pointers: O(n) time and O(1) space

        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l<r:
            #always move the one with a lower value
            if leftMax < rightMax:
                l += 1
                #the order of the following lines
                #makes sure the res > 0
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res

        #O(n) time and space
        max_left = 0
        max_right = 0
        leftmax = []
        rightmax = []
        res = 0

        for l in range(len(height)):
            leftmax.append(max_left)
            max_left = max(max_left, height[l])

        for r in range(len(height) -1, -1, -1):
            rightmax.append(max_right)
            max_right = max(max_right, height[r])  

        rightmax = rightmax[::-1]

        for i in range(len(height)):
            trapped_water = min(leftmax[i], rightmax[i]) - height[i]
            if trapped_water < 0:
                continue
            else:
                res += trapped_water













        # Using O(n) time and space

        if not height: return 0

        maxL = 0
        maxR = 0
        maxLeft = []
        maxRight = []
        minList = []
        output = 0

        for i in range(len(height)):
            maxL = max(maxL, height[i])
            maxLeft.append(maxL)

        for i in range(len(height) - 1, -1, -1):
            maxR = max(maxR, height[i])
            maxRight.append(maxR)

        maxRight.reverse()

        for i in range(len(maxLeft)):
            minval = min(maxLeft[i], maxRight[i])
            minList.append(minval)
        
        for i in range(len(minList)):
            res = minList[i] - height[i]
            if res < 0:
                res = 0
            output += res
        return output
            


        # O(n) time and constant O(1) space
        # Optimization using two pointers
        # if not height: return 0

        # l, r = 0, len(height) - 1
        # leftMax, rightMax = height[l], height[r]
        # res = 0

        # while l < r:
        #     if leftMax < rightMax:
        #         l += 1
        #         leftMax = max(leftMax, height[l])
        #         res += leftMax - height[l]
        #     else:
        #         r -= 1
        #         rightMax = max(rightMax, height[r])
        #         res += rightMax - height[r]
        # return res


        # O(n) & O(1) - Does not work
        # if not height:
        #     return 0

        # l, r = 0, len(height) - 1
        # maxLeft, maxRight = height[l], height[r]
        # res = 0

        # while l < r:
        #     maxLeft = max(maxLeft, height[l])
        #     maxRight = max(maxRight, height[r])
        #     water = min(maxLeft, maxRight) - height[l]
        #     if water < 0:
        #         water = 0
        #         res += water
        #     else:
        #         res += water
        #     l += 1
        #     r -= 1
        # return res


        