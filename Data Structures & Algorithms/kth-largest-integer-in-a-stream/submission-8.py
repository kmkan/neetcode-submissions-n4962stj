import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = []
        heapq.heapify(self.stream)
        self.k = k

        for n in nums:
            if len(self.stream) < self.k:
                heapq.heappush(self.stream, n)
            else:
                heapq.heappushpop(self.stream, n)

    def add(self, val: int) -> int:
        if len(self.stream) < self.k:
            heapq.heappush(self.stream, val)
        else:
            heapq.heappushpop(self.stream, val)

        return self.stream[0]
