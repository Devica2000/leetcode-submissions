class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r)//2
            if target == nums[m]:
                return m 
            elif target > nums[m]:
                l += 1
            else:
                r -= 1
        return -1










        # Time Complexity = O(log n)
        l = 0
        r = len(nums) - 1
        while l <= r:
            #In other languages, this could lead to overflow
            #To avoid that, we use distance instead 
            #m = l + ((r-l)//2)
            m = (l + r)//2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        return -1
        
        #Time Complexity = O(n)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        