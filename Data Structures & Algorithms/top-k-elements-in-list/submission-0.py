class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = {}

        for num in nums:
            freq_nums[num] = freq_nums.get(num, 0) + 1
        
        freq_num_pairs = sorted(list(freq_nums.items()), key=lambda x: x[1])
        ans = []
        print(freq_num_pairs)
        for i in range(len(freq_num_pairs) - 1, len(freq_num_pairs) - 1 - k, -1):   
            ans.append(freq_num_pairs[i][0])
            print(freq_num_pairs[i])
        return ans