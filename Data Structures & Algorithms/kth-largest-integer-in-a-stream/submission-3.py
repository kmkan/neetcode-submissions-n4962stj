import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        for i in range(len(nums)):
            nums[i] *= -1
        self.stream = nums
        heapq.heapify(self.stream)
        self.k = k
        print(self.stream)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val * -1)

        vals = []

        for i in range(self.k):
            vals.append(heapq.heappop(self.stream))
        
        ans = vals[-1]
        for v in vals:
            heapq.heappush(self.stream, v)
        
        return ans * -1
