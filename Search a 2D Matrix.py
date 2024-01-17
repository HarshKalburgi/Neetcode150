# Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            r = len(matrix[i]) - 1
            l = 0
            arr = matrix[i]
            check = True
            if target > arr[len(arr) - 1]:
                check = False
            while l <= r and check:
                mid = l + (r - l) // 2

                if arr[mid] == target:
                    return True

                elif arr[mid] < target:
                    l = mid + 1

                else:
                    r = mid - 1

        return False