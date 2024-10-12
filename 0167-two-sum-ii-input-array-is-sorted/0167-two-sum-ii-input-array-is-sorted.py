class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Two Pointer - O(n)
        l = 0
        r = len(numbers) - 1

        while l<r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return


        #Brute force - O(n^2)
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return

        