class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        Rows, Cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if(nr < 0 or nc < 0 or nr >= Rows or 
                        nc >= Cols or grid[nr][nc] == "0"
                        ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands