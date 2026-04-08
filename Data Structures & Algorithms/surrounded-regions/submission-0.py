class Solution:
    def solve(self, board):
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != 'O'):
                return

            board[r][c] = '#'

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Step 1: mark border-connected 'O'
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Step 2: flip + restore
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'