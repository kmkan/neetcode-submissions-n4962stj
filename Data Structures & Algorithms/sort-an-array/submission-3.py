class Solution:
    def mergeSort(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return arr
        
        n = len(arr)

        left = self.mergeSort(arr[:n // 2])
        right = self.mergeSort(arr[n // 2:])

        return self.merge(left, right)
    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = 0
        j = 0
        ans = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
        
        ans += arr1[i:]
        ans += arr2[j:]

        return ans
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        