direction = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

class Solution:
    def dfs(self, grid, start, visited, start_sides):
        if start in visited:
            return 0
        rows, cols = len(grid), len(grid[0])
        cur_r, cur_c = start

        visited.add(start)
        new_total = 0
        for dr, dc in direction:
            new_r, new_c = cur_r + dr, cur_c + dc

            if (0 <= new_r < rows) and (0 <= new_c < cols):
                if grid[new_r][new_c] == 1:
                    start_sides -= 1
                
                    if (new_r, new_c) not in visited:
                        new_total += self.dfs(grid, (new_r, new_c), visited, 4)
        return new_total + start_sides
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        p = 0
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    p += self.dfs(grid, (i, j), visited, 4)   
        return p
                