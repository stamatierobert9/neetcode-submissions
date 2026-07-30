class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        
        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or 
                r < 0 or c < 0 or r == Rows or c == Cols or
                heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(Cols):
            dfs(0, c, pac, heights[0][c])
            dfs(Rows - 1, c, atl, heights[Rows - 1][c])
        
        for r in range(Rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, Cols - 1, atl, heights[r][Cols - 1])
        
        res = []
        for r in range(Rows):
            for c in range(Cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])

        return res