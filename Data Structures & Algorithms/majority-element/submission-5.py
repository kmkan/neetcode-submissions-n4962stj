class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ele = None
        cur_count = 0

        for num in nums:
            if cur_count == 0:
                maj_ele = num
            
            if num == maj_ele:
                cur_count += 1
            else:
                cur_count -= 1


        return maj_ele
