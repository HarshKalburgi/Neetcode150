# Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 
# code
import collections
class Solution(object):
    def isValidSudoku(self, board):
        cols = [collections.defaultdict(int) for _ in range(9)]
        rows = [collections.defaultdict(int) for _ in range(9)]
        squares = [collections.defaultdict(int) for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = int(board[r][c])
                    square_index = (r // 3) * 3 + c // 3
                    if rows[r][num] or cols[c][num] or squares[square_index][num]:
                        return False
                    rows[r][num] = 1
                    cols[c][num] = 1
                    squares[square_index][num] = 1
        return True
