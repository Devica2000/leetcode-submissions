class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count = {}

        for num in nums:
            if num in num_count:
                return True
            else:
                num_count[num] = True
        return False



        return len(nums) != len(set(nums))

        #using a hashmap
        count_nums = {}
        for n in nums:
            if n in count_nums:
                count_nums[n] += 1
            else:
                count_nums[n] = 1
        
        for val in count_nums.values():
            if val > 1:
                return True
        return False
            


        














        # Solution 1: Using a set()
        # if len(set(nums)) != len(nums):
        #     return True
        # return False

        # Solution 2: Using a hashmap
        # Hashmap to store num:count pairs
        # num_counts = {} 

        # for num in nums:
        #     if num not in num_counts:
        #         num_counts[num] = 1
        #     else:
        #         num_counts[num] += 1

        # for count in num_counts.values():
        #     if count > 1:
        #         return True
        # return False

        # # Using hashmap
        # count = {}
        # for n in nums:
        #     if n in count:
        #         return True
        #     else:
        #         count[n] = True
        # return False

        #Brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Using sorting - O(nlogn) and O(1)
        # nums = sorted(nums)

        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        # Using a hashmap
        # O(n) time and space
        val_count = {}

        for num in nums:
            if num not in val_count:
                val_count[num] = True
            else:
                return True
        return False

        # Keep a count of the elements
        # O(n) time and O(n) space
        # O(n) - worst case store all elements in case of no duplicates

        # val_count = {}

        # for num in nums:
        #     if num not in val_count:
        #         val_count[num] = 1
        #     else:
        #         val_count[num] += 1

        # for count in val_count.values():
        #     if count > 1:
        #         return True
        # return False

        # Using hashset -  O(n) time and space

        # hashset = set()

        # for num in nums:
        #     if num in hashset:
        #         return True
        #     hashset.add(num)
        # return False