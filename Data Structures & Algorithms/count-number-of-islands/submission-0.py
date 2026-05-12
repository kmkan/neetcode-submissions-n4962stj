directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

class Solution:
    def dfs(self, grid, start, visited):
        if start in visited:
            return
        
        visited.add(start)

        rows, cols = len(grid), len(grid[0])

        for dr, dc in directions:
            cur_r, cur_c = start[0] + dr, start[1] + dc

            if (0 <= cur_r < rows) and (0 <= cur_c < cols):
                if (cur_r, cur_c) not in visited and grid[cur_r][cur_c] == '1':
                    self.dfs(grid, (cur_r, cur_c), visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        total = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == '1':
                    total += 1
                    self.dfs(grid, (i, j), visited)
        
        return total