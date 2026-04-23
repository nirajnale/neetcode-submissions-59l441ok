class Solution:
    def spiralOrder(self, matrix):
        res = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res