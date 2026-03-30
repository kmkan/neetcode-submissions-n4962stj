class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = nums[0]
        majority_count = 0

        for num in nums:
            if majority_count == 0:
                majority_element = num
            if num == majority_element:
                majority_count += 1
            else:
                majority_count -= 1
        return majority_element