class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            d = math.sqrt(p[0] ** 2 + p[1] ** 2)
            heap.append((d, p))

        heapq.heapify(heap)

        ans = []

        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        
        return ans