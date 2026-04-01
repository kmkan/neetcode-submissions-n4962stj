class Solution:
    def merge(self, start1: int, end1: int, start2: int, end2: int, arr: List[int]) -> List[int]:
        i = start1
        j = start2
        ans = []
        while i < end1 and j < end2:
            if arr[i] <= arr[j]:
                ans.append(arr[i])
                i += 1
            else:
                ans.append(arr[j])
                j += 1
        
        while i < end1:
            ans.append(arr[i])
            i += 1
        while j < end2:
            ans.append(arr[j])
            j += 1
        
        for i in range(start1, end2):
            arr[i] = ans[i - start1]
        return arr
    def mergeSort(self, arr: List[int], start: int, end: int) -> List[int]:

        if end - start <= 1:
            return arr

        left = self.mergeSort(arr, start, (start + end) // 2)
        right = self.mergeSort(arr, (start + end) // 2, end)

        return self.merge(start, (start + end) // 2, (start + end) // 2, end, arr)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums))