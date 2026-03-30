class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
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
        
        while i < len(arr1):
            ans.append(arr1[i])
            i += 1
        while j < len(arr2):
            ans.append(arr2[j])
            j += 1
        
        return ans
    def mergesort(self, arr: List[int]) -> List[int]:
        n = len(arr)

        if n == 1:
            return arr
        
        
        left = arr[:n // 2]
        right = arr[n // 2:]

        sorted_left = self.mergesort(left)
        sorted_right = self.mergesort(right)
        
        return self.merge(sorted_left, sorted_right)