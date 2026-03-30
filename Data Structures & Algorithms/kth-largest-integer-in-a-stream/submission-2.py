import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = [n * -1 for n in nums]
        heapq.heapify(self.stream)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val * -1)
        vals = []

        for i in range(self.k):
            vals.append(heapq.heappop(self.stream))
        
        ans = vals[-1]
        for i in range(self.k):
            heapq.heappush(self.stream, vals[i])
        
        print(self.stream)
        return ans * -1

