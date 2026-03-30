class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: Reverse vertically
        matrix.reverse()

        # Step 2: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
