class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we need to do a couple in-place transformations! 
        
        N: int = len(matrix)
        
        for i in range(N):
            for j in range(i):
                # we first need to do the transpose with a swap 
                n1: int = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = n1
                
        for i in range(N):
            for j in range(floor(N/2)):
                # and now we need to swap the columns! 
                n1: int = matrix[i][j]
                matrix[i][j] = matrix[i][N-1-j]
                matrix[i][N-1-j] = n1
