import heapq
import math
class Solution:
    def e(self, x1: int, y1: int, x2: int = 0, y2: int = 0) -> float:
        return math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_points = []
        heapq.heapify(heap_points)


        for p in points:
            distance = self.e(p[0], p[1])
            heapq.heappush(heap_points, (distance, (p[0], p[1])))
        
        ans = []

        for i in range(k):
            cur = heapq.heappop(heap_points)
            p = [cur[1][0], cur[1][1]]
            ans.append(p)
        
        return ans