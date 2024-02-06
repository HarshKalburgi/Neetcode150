# Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

#  code

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= columns or grid[row][col] ==0:
                return 
            grid[row][col] = 0
            a[0] += 1
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
            return a[0]
        MAX=0             
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1:
                    a=[0]
                    A=dfs(row,col)
                    MAX=max(A,MAX)
               
        return MAX