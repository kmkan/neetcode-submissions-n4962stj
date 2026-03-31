class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        list_count = [(v, k) for k, v in count.items()]
        return max(list_count)[1]
