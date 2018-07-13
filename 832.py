class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for a in A:
            a.reverse()
            # result.append([int(not bool(item)) for item in a])
            # result.append([1-item for item in a])
            result.append([item ^ 1 for item in a])
        return result

# 取反
#        for row in A:
#            for i in range(int((len(row) + 1) / 2)):
#                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
#        return A


if __name__ == '__main__':
    solution = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(solution.flipAndInvertImage(A) == [[1,0,0],[0,1,0],[1,1,1]])
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(solution.flipAndInvertImage(A) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]])
