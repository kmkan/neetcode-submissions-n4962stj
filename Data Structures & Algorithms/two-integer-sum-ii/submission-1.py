class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pos_nums = {}
        
        for i in range(len(numbers)):
            k = target - numbers[i]
            if k in pos_nums:
                return [pos_nums[k] + 1, i + 1]
            
            pos_nums[numbers[i]] = i
        
        