class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            validation = [0] * 9
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                idx = int(c) - 1
                if idx < 0 or idx > 8:
                    return False
                if validation[idx]:
                    return False
                validation[idx] = 1

        for i in range(9):
            validation = [0] * 9
            for j in range(9):
                c = board[j][i]
                if c == '.':
                    continue
                idx = int(c) - 1
                if idx < 0 or idx > 8:
                    return False
                if validation[idx]:
                    return False
                validation[idx] = 1

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                validation = [0] * 9
                for di in range(3):
                    for dj in range(3):
                        c = board[i + di][j + dj]
                        if c == '.':
                            continue
                        idx = int(c) - 1
                        if idx < 0 or idx > 8:
                            return False
                        if validation[idx]:
                            return False
                        validation[idx] = 1

        return True