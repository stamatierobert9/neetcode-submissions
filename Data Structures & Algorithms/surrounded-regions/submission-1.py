class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Rows, Cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture(r, c):
            if (r < 0 or c < 0 or r == Rows or
                c == Cols or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            for dr, dc in directions:
                capture(r + dr, c + dc)

        for r in range(Rows):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][Cols - 1] == "O":
                capture(r, Cols - 1)

        for c in range(Cols):
            if board[0][c] == "O":
                capture(0, c)
            if board[Rows - 1][c] == "O":
                capture(Rows - 1, c)

        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        