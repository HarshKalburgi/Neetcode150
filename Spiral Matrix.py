# Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
# code

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        mm, nn = 1, 0
        while m - mm >= 0 and n - nn > 0:
            horizontal = True
            if nn % 2 == 0: # ascending

                for i in range((mm+1)//2-1, m-((mm+1)//2)+1):
                    
                    if horizontal:
                        for j in range(nn//2, n-(nn//2)):
                            
                            result.append(matrix[i][j])
                            if j == n-(nn//2)-1: horizontal = False
                    else:
                        
                        result.append(matrix[i][n-(nn//2)-1])
            else: # descending
                
                for i in range(m-(mm//2), (mm//2)-1, -1):

                    if horizontal:
                        for j in range(n-(nn//2)-2, (nn//2)-1, -1):
                            
                            result.append(matrix[i][j])
                            if j == (nn//2): horizontal = False
                    else:
                        
                        result.append(matrix[i][(nn//2)])
            
            mm += 1
            nn += 1
            
        return result
        