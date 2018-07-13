class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        result = [[A[j][i] for j in range(row)] for i in range(col)]
        return result
#       return [list(item) for item in zip(*A)]

if __name__ == '__main__':
    print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().transpose([[1,2,3],[4,5,6]]))
