class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)

        ans = []

        for i in range(len(nums)):
            cur_nums = {}
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in cur_nums:
                    ans.append([nums[i], nums[cur_nums[-(nums[i] + nums[j])]], nums[j]])
                    del cur_nums[-(nums[i] + nums[j])]
                else:
                    cur_nums[nums[j]] = j
        return ans