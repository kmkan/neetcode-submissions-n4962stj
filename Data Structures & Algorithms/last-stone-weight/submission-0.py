import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [s * -1 for s in stones]
        heapq.heapify(stones)
        print(stones)
        while stones and len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            print(x, y, stones)
            if x == y:
                continue
            else:
                x -= y
                heapq.heappush(stones, x)
        
        if stones:
            return -1 * stones[0]
        
        return 0