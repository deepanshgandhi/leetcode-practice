class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        def dfs(i,j):
            grid[i][j]=0
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for dr,dc in directions:
                nr,nc=(i+dr),(j+dc)
                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc]==1:
                    dfs(nr,nc)

        for j in range(COLS):
            if grid[0][j]==1:
                dfs(0,j)
            if grid[ROWS-1][j]==1:
                dfs(ROWS-1,j)
        for i in range(ROWS):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][COLS-1]==1:
                dfs(i,COLS-1)
        ones=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    ones+=1
        return ones
        