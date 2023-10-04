class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Brute Force - O(n^2)
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     for val in range(i+1, len(nums)):
        #         if nums[val] == diff:
        #             return [i, val]

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        
        #Using hashmap
        # Time becomes linear - O(n)

        idx_val = {} #hashmap to store the val:idx pairs
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in idx_val:
                return [idx_val[diff], idx]
            idx_val[num] = idx
        return #not necessary since we are guaranteed that a solution exists