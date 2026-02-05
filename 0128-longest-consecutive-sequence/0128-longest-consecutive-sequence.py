class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        sorted_nums = sorted(nums)
        best = 1
        current = 1

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i+1] == sorted_nums[i] + 1:
                current += 1
            elif sorted_nums[i+1] != sorted_nums[i]:
                current = 1
            best = max(best, current)

        return best
        





























        #Use a hash set to keep track of the unique numbers in nums

        numSet = set(nums)
        longest, length = 0, 0

        for num in numSet:
            #check if this number is the start of a sequence
            if (num - 1) not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
            longest = max(longest, length)
        return longest

        # Without initializing length
        # longest within the if condition

        numSet = set(nums)
        longest = 0

        for num in numSet:
            #check if this number is the start of a sequence
            if (num - 1) not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest




        num_set = set(nums)
        longest_length = 0
        for num in num_set:
            if (num - 1) not in num_set:
                curr_num = num
                current_length = 1
                while (curr_num + 1) in num_set:
                    curr_num += 1
                    current_length += 1
                longest_length = max(longest_length, current_length)
        return longest_length



        # Using set - O(n)
        numSet = set(nums)
        longest = 0
        
        for n in numSet:
            #check the left value to see if it is the start of the sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

        # if not nums:
        #     return 0

        # num_set = set(nums)
        # longest_streak = 0

        # for num in num_set:
        #     if num - 1 not in num_set:
        #         current_num = num
        #         current_streak = 1

        #         while current_num + 1 in num_set:
        #             current_num += 1
        #             current_streak += 1

        #         longest_streak = max(longest_streak, current_streak)
        
        # return longest_streak