class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) time and O(1) space
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


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


        