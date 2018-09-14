class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        for row in range(rows - 1):
            if matrix[row][:-1] != matrix[row + 1][1:]:
                return False
        else:
            return True
