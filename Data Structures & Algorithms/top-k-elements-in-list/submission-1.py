import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}

        for n in nums:
            count_nums[n] = count_nums.get(n, 0) + 1
        
        heap = [(v * -1, k) for k, v in count_nums.items()]

        heapq.heapify(heap)
        ans = []

        for i in range(k):
            top = heapq.heappop(heap)
            ans.append(top[1])
        
        return ans

