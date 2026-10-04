class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        heap = []
        for key in count.keys():
            heapq.heappush(heap, (count[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            key, val = heapq.heappop(heap)
            res.append(val)
        return res
