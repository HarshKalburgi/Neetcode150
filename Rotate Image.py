# Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# code
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        def reverse(row):
            left = 0
            right = len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
        for i in range(rows): # Transpose the matrix
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(rows): # Reverse every row in the transposed matrix
            reverse(matrix[i])
        