class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxx = 0
        def dfs(i,j):
            if  i < 0 or i >= m  or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            else:
                grid[i][j] = 0
                return 1 +  dfs(i+1,j) +  dfs(i-1,j)  +  dfs(i,j+1)  +  dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxx = max(maxx,dfs(i,j))


        print(maxx)


# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid =   [[1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]]
s = Solution().maxAreaOfIsland(grid)