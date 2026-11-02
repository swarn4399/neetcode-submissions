class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def DFS(grid, row, col):
            if (row<0 or row>=len(grid)) or (col<0 or col>=len(grid[0])) or grid[row][col]!='1':
                return
            grid[row][col] = '0'
            DFS(grid, row-1, col)
            DFS(grid, row+1, col)
            DFS(grid, row, col-1)
            DFS(grid, row, col+1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count+=1
                    DFS(grid, row, col)

        return count