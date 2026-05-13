direction = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

class Solution:
    def dfs(self, grid, start, visited):
        if start in visited:
            return 0
        
        visited.add(start)

        cur_r, cur_c = start
        rows, cols = len(grid), len(grid[0])
        area = 0
        for dr, dc in direction:
            new_r, new_c = cur_r + dr, cur_c + dc

            if (0 <= new_r < rows) and (0 <= new_c < cols):
                if grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                    area = area + self.dfs(grid, (new_r, new_c), visited)

        return area + 1
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, (i, j), visited))
        
        return max_area
        