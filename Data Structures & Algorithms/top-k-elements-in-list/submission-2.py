import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}

        for n in nums:
            count_nums[n] = count_nums.get(n, 0) + 1
        
        heap = []

        heapq.heapify(heap)
        ans = []

        for key, v in count_nums.items():
            heapq.heappush(heap, (v, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        
        return [h[1] for h in heap]

