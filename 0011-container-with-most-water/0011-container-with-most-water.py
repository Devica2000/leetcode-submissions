class Solution:
    def maxArea(self, height: List[int]) -> int:
        #linear time - O(n)
        max_area = 0
        l, r = 0, len(height) - 1

        while l<r:
            area = (r-l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] > height[r]:
                r -= 1
            elif height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_area


        #Brute Force - O(n^2)
        max_area = 0
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r-l) * min(height[l], height[r])
                max_area = max(max_area, area)
        return max_area















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



        