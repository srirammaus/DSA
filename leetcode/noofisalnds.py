

"""
200. Number of Islands
Medium
Topics
premium lock icon
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
class Solution:
    def numIslands(self, grid:list[list[str]]):
        m = len(grid)
        n = len(grid[0])
        count = 0
        def dfs(i,j):
            if  i < 0 or i >= m  or j < 0 or j >= n or grid[i][j] != "1":
                return
            else:
                grid[i][j] = "0"
                dfs(i+1,j) #down
                dfs(i-1,j) # up
                dfs(i,j+1)  #right
                dfs(i,j-1)  #left
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        return count






grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
soln = Solution().numIslands(grid)

print(soln)
