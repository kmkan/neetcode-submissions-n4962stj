class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rank = []
        heapq.heapify(rank)

        for n in nums:
            if len(rank) < k:
                heapq.heappush(rank, n)
            else:
                heapq.heappushpop(rank, n)
        
        return rank[0]