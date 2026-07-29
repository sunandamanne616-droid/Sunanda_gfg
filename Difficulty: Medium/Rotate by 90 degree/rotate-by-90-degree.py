class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each column
        for j in range(n):
            top, bottom = 0, n - 1
            while top < bottom:
                matrix[top][j], matrix[bottom][j] = matrix[bottom][j], matrix[top][j]
                top += 1
                bottom -= 1

        return matrix