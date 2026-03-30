import heapq
import math
class Solution:
    def e(self, x1: int, y1: int, x2: int = 0, y2: int = 0) -> float:
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_points = []
        heapq.heapify(heap_points)


        for i, p in enumerate(points):
            distance = self.e(p[0], p[1])
            heapq.heappush(heap_points, (distance, i))
        
        ans = []
        print(heap_points)
        for i in range(k):
            cur = heapq.heappop(heap_points)
            print(cur)
            ans.append(points[cur[1]])
        
        return ans