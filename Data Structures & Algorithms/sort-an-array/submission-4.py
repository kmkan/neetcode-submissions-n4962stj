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
    def mergeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)

        if n == 1:
            return arr
        
        left = arr[:n // 2]
        right = arr[n // 2:]

        left = self.mergeSort(left)
        right = self.mergeSort(right)

        return self.merge(left, right)
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        