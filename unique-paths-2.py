class Solution:
    def __init__(self):
        self.results = []

    def _recurse(self, x, y, grid, sequence):
        # you are at x,y with sequence
        if grid[y][x] == 1:
            return
        if y == len(grid) - 1 and x == len(grid[0]) - 1:
            self.results.append(sequence)
            print(f"FOUND {x}, {y} with {sequence}")
            return
        print(f"At {x}, {y} with {sequence}")
        if y + 1 < len(grid):
            self._recurse(x, y + 1, grid, sequence + "d")
        if x + 1 < len(grid[0]):
            self._recurse(x + 1, y, grid, sequence + "r")

    def uniquePathsWithObstacles(self, obstacleGrid):
        self._recurse(0, 0, obstacleGrid, "")
        return len(self.results)


# You are given an m x n integer array grid.
# There is a robot initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid.
# A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

sol = Solution()
# sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

sol.uniquePathsWithObstacles([[0, 1], [0, 0]])
sol.uniquePathsWithObstacles([[0, 0], [0, 1]])
