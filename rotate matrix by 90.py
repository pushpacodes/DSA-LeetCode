class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        temp = [row[:] for row in matrix]
        for i in range(r):
            for j in range(c):
                matrix[j][r-1-i] = temp[i][j]
