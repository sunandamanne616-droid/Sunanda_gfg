class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)
        new = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                new[n - 1 - j][i] = mat[i][j]

        for i in range(n):
            for j in range(n):
                mat[i][j] = new[i][j]