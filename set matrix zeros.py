###brute force
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    self.markinfinity(matrix,i,j)
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=0
    def markinfinity(self,matrix,row,col):
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            if matrix[i][col]!=0:
                matrix[i][col]=float('inf')
        for i in range(c):
            if matrix[row][i]!=0:
                matrix[row][i]=float('inf')
###optimal solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        rowmat=[0]*r
        colmat=[0]*c
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rowmat[i]=-1
                    colmat[j]=-1
        for i in range(r):
            for j in range(c):
                if rowmat[i]==-1 or colmat[j]==-1:
                    matrix[i][j]=0
