# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid) -> int:
        # check if grid first
        if not grid:
            return 0
        # define the rows and the cols of the grid
        rows, cols = len(grid), len(grid[0])
        # initialize a set that will be used to check where we have already covered
        visited = set()
        # final number of islands
        islands = 0
        # directions when looping through an island
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r,c):
            # mark the current row as visited
            visited.add((r,c))
            # explore all the directions of the that square in the island -> neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # check if the neighbor square is with the bounds and valid island and is not visited
                if (
                    (nr in range(rows)) 
                    and (nc in range(cols))
                    and grid[nr][nc] == "1" 
                    and (nr, nc) not in visited):
                        # valid island neighbor, visit it and recurse until not valid
                        dfs(nr,nc)

        # go through all the cols and rows
        for r in range(rows):
            for c in range(cols):
                # if a row and col hasn't been visited yet, visit it using dfs
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r,c)
                    # once exhausted all the islands there, increment our value
                    islands += 1

        return islands
