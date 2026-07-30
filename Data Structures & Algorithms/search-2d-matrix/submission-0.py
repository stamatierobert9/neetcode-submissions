class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])
        l, r = 0, Rows * Cols - 1

        while l <= r:
            m = l + (r - l) // 2
            row, col = m // Cols, m % Cols

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False