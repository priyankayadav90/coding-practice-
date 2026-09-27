class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty_count = 0
        start_r, start_c = 0, 0

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    empty_count += 1
                elif grid[r][c] == 0:
                    empty_count += 1

        def dfs(r, c, count):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1:
                return 0
            
            
            if grid[r][c] == 2:
                
                return 1 if count == empty_count else 0

    
            temp = grid[r][c]
            grid[r][c] = -1
            count += 1

            
            total_paths = (
                dfs(r + 1, c, count) +
                dfs(r - 1, c, count) +
                dfs(r, c + 1, count) +
                dfs(r, c - 1, count)
            )

            
            grid[r][c] = temp
            return total_paths

        return dfs(start_r, start_c, 0)
