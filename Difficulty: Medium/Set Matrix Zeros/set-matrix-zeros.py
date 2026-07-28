class Solution:
    def setMatrixZeroes(self, mat):
        r = len(mat)
        m = len(mat[0])

        def makerow(row):
            for j in range(m):
                if mat[row][j] != 0:
                    mat[row][j] = "_"

        def makecol(col):
            for i in range(r):
                if mat[i][col] != 0:
                    mat[i][col] = "_"

        for i in range(r):
            for j in range(m):
                if mat[i][j] == 0:
                    makerow(i)
                    makecol(j)

        # Convert markers to 0
        for i in range(r):
            for j in range(m):
                if mat[i][j] == "_":
                    mat[i][j] = 0

        return mat