# Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# # code

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        V = []

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    V.append((i, j))

        for row, col in V:
            matrix[row] = [0] * m

            for i in range(n):
                matrix[i][col] = 0