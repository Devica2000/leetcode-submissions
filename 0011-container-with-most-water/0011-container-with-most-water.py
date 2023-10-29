class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Sorting - O(n)
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            max_prod = (r - l) * min(height[r], height[l])
            max_area = max(max_area, max_prod)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1    
            # could be condensed in the above   
            else:
                r -= 1         
        return max_area
            
        #brute force - O(n^2)
        # max_area = 0

        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         max_water = ((j - i) * min(height[i], height[j]))
        #         max_area = max(max_area, max_water)
        # return max_area



        