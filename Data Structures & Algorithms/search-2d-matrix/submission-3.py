class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1
        print(m, n)
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // n
            col = mid % n

            print(f'Mid: {mid}, Left: {left}, Right: {right}, Row: {row}, Col: {col}, Item: {matrix[row][col]}')
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
