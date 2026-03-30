import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        ans = None

        while k > 0:
            ans = heapq.heappop(nums)
            k -= 1
        return ans * -1