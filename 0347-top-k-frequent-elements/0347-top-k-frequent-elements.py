class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}

        for num in nums:
            if num not in countmap:
                countmap[num] = 1
            else:
                countmap[num] += 1
        
        sorted_dict = dict(sorted(countmap.items(), key = lambda x: x[1], reverse =True))
        output_keys = list(sorted_dict.keys())
        return output_keys[:k]