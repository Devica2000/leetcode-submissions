class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:










        
        #Time Complexity = O(log(max p) * p)
        #Given: len(piles) <= h  
        #Koko only eats at most 1 pile of bananas in 1 hour
        #min k = 1
        #To finish everything in <= h hours, Max k = max(piles)

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1
        return res

        #brute force - O(n^2)
        # for num in range(1, max(piles) + 1):
        #     hours = 0
        #     for p in piles:
        #         hours += math.ceil(p/num)
        #     if hours <= h:
        #         return num


        