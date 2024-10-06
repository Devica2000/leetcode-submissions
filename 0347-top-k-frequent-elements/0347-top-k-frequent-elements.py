class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Using Bucket Sort

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, c in count.items():
            freq[c].append(num)

        res = []

        #we need to look for numbers from the end to the start (desc order)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res



        # num_count = {}

        # for num in nums:
        #     if num not in num_count:
        #         num_count[num] = 1
        #     else:
        #         num_count[num] += 1
        
        # sorted_counts = dict(sorted(num_count.items(), key=lambda item: item[1], reverse = True))
        # return list(sorted_counts.keys())[:k]

        # count = Counter(nums)
        # # Use a max heap to get the k most frequent elements
        # # Since heapq is a min-heap, we can use negative frequencies
        # max_heap = [(-freq, num) for num, freq in count.items()]
        # # Create the heap
        # heapq.heapify(max_heap)
        # # Extract the top k elements
        # result = []
        # for _ in range(k):
        #     freq, num = heapq.heappop(max_heap)
        #     result.append(num)
        # return result










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


