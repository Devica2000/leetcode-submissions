class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # O(n)
        hashnum = set(nums)
        if len(nums) == len(hashnum):
            return False
        return True

        # the process of converting list nums to set expanded
        # O(n)
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        