class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity = O(n)
        nums.sort()
        output = []

        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue

            l, r = idx + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return output


        # #brute force - O(n^3)
        # output = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j+ 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0 :
        #                 triplets = [nums[i],nums[j],nums[k]]
        #                 #check if the triplet is already present in the output list
        #                 #or if any sorted version of the triplets is present in the 
        #                 #sorted elements of the output list
        #                 if triplets not in output and sorted(triplets) not in [sorted(existing_triplets) for existing_triplets in output]:
        #                     output.append(triplets)
        # return output

