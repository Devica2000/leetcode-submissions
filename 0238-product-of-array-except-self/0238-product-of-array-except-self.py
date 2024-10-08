class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time and O(1) space
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        # #O(n) time and space
        # n = len(nums)
        # if n == 0:
        #     return []

        # prefix = [1] * n
        # postfix = [1] * n
        # res = [0] * n

        # # Calculate prefix products
        # for i in range(1, n):
        #     prefix[i] = prefix[i - 1] * nums[i - 1]

        # # Calculate postfix products
        # for i in range(n - 2, -1, -1):
        #     postfix[i] = postfix[i + 1] * nums[i + 1]

        # # Combine prefix and postfix products
        # for i in range(n):
        #     res[i] = prefix[i] * postfix[i]

        # return res


        # O(n) time and O(1) space

        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        # # brute force O(n)- using division 
        # product = 1
        # output_list = []
        # zero_count = 0

        # for num in nums:
        #     if num != 0:
        #         product *= num
        #     else:
        #         zero_count += 1

        # for num in nums:
        #     if zero_count > 1:
        #         output_list.append(0)
        #     elif zero_count == 1:
        #         if num == 0:
        #             output_list.append(product)
        #         else:
        #             output_list.append(0)
        #     else:
        #         output_list.append(product//num)
        # return output_list