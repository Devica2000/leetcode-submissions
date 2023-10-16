class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Use a set since set stores the unique elements
        # Check the length of the set and the list
        # if they are equal -> all elements are unique
        # if not, there are duplicates
        # Linear time algo 
        # converting list -> O(n)

        num_set = set(nums) 

        #O(1)
        if len(nums) == len(num_set): 
            return False
        else:
            return True

        #Brute force - O(n2)
        # if len(nums) == 1:
        #     return False
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Using hashSet - Neetcode solution
        # O(n)

        # hashset = set()
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False