# N-Queens
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
# code

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        result = []
        col = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                board[r][c] = 'Q'
                col.add(c)
                posDiag.add((r + c))
                negDiag.add((r - c))

                backtrack(r + 1)

                board[r][c] = '.'
                col.remove(c)
                posDiag.remove((r + c))
                negDiag.remove((r - c))

        backtrack(0)
        return result



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.'] * n for i in range(n)]
        cols = set()
        posDiag = set()
        negDiag = set()
        result = []

        def backtrack(r):
            if r == n:
                result.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                board[r][c] = 'Q'
                cols.add(c)
                posDiag.add((r + c))
                negDiag.add((r - c))

                backtrack(r + 1)

                board[r][c] = '.'
                cols.remove(c)
                posDiag.remove((r + c))
                negDiag.remove((r - c))

        
        backtrack(0)
        return result


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        board = [['.'] * n for i in range(n)]
        cols = set()
        postDiag = set()
        negDiag = set()

        def backtrack(r):
            if r == n:
                result.append([''.join(row) for row in board])
                return 

            for c in range(n):
                if c in cols or (r + c) in postDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                postDiag.add((r + c))
                negDiag.add((r - c))

                board[r][c] = 'Q'

                backtrack(r + 1)

                cols.remove(c)
                postDiag.remove((r + c))
                negDiag.remove((r - c))

                board[r][c] = '.'

        backtrack(0)
        return result

                