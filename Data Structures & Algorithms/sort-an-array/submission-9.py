class Solution:
    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr1)
        m = len(arr2)
        i = 0
        j = 0
        ans = []

        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
        
        while i < n:
            ans.append(arr1[i])
            i += 1
        while j < m:
            ans.append(arr2[j])
            j += 1
        
        return ans

    def mergeSort(self, arr: List[int], begin: int, end: int) -> List[int]:
        if begin == end:
            return [arr[begin]]
        if begin > end:
            return []
        
        left = self.mergeSort(arr, begin, (begin + end) // 2)
        right = self.mergeSort(arr, (begin + end) // 2 + 1, end)

        return self.merge(left, right)
        

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)
        