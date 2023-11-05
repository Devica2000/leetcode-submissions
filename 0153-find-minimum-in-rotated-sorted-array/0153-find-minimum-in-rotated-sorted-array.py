class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        res = nums[0]

        while l<=r:
            if nums[l] < nums[r]:
                #this means that the array is sorted
                res = min(res, nums[l])
                break
            
            #if we are in rotated sorted array - binary search
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                #means we are in the left sorted array
                #need to search right
                l = m + 1
            else:
                r = m - 1
        return res 