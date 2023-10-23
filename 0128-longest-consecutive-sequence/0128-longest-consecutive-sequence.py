class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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