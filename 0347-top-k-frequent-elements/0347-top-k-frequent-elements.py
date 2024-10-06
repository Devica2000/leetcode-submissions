class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count = {}

        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
        
        sorted_counts = dict(sorted(num_count.items(), key=lambda item: item[1], reverse = True))
        return list(sorted_counts.keys())[:k]












        # Linear Time - O(n)
        count = {}  #hashmap to keep track of the count of elements
        freq = [[] for i in range(len(nums) + 1)] #bucket sort special array

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(nlogn)
        # countmap = {}

        # for num in nums:
        #     countmap[num] = 1+ countmap.get(num, 0)
        #     # if num not in countmap:
        #     #     countmap[num] = 1
        #     # else:
        #     #     countmap[num] += 1
        
        # sorted_dict = dict(sorted(countmap.items(), key = lambda x: x[1], reverse =True))
        # output_keys = list(sorted_dict.keys())
        # return output_keys[:k]


