class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or heights[r][c] < prevHeight):
                return

            visited.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Pacific (top + left)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])

        return [[r, c] for r in range(rows)
                for c in range(cols)
                if (r, c) in pacific and (r, c) in atlantic]
                