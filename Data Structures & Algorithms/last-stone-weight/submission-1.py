import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while stones and len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x == y:
                continue
            else:
                x -= y
                heapq.heappush(stones, x)
        
        if stones:
            return -1 * stones[0]
        
        return 0