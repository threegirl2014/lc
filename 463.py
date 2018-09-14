class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        rows = len(grid)
        columns = len(grid[0])
        for row in range(rows):
            for column in range(columns):
                if grid[row][column]:
                    result += 4
                    if row > 0 and grid[row - 1][column]:
                        result -= 1
                    if row < rows - 1 and grid[row + 1][column]:
                        result -= 1
                    if column > 0 and grid[row][column - 1]:
                        result -= 1
                    if column < columns - 1 and grid[row][column + 1]:
                        result -= 1
        return result
