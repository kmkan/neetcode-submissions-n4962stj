class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        length = len(nums)
        ans = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for k, v in count.items():
            print(f'{k}: {v}, n // 3: {n // 3}')
            if v > length // 3:
                ans.append(k)
        
        return ans