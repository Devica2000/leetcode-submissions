class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1,r + 1]


        # numIndex = {}
        # for idx, num in enumerate(numbers):
        #     diff = target - num
        #     if diff in numIndex:
        #         return([numIndex[diff] + 1, idx + 1])
        #     numIndex[num] = idx
        # return 0

 