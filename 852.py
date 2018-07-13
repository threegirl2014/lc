class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
#        for i in range(1, len(A) - 1):
#            if A[i - 1] < A[i] and A[i] > A[i + 1]:
#                return i

#        r = 0
#        for i in range(1, len(A) - 1):
#            if A[i - 1] < A[i]:
#                r = i
#            else:
#                break
#        return r

        return A.index(max(A))


if __name__ == '__main__':
    solution = Solution()
    A = [0,1,0]
    print(solution.peakIndexInMountainArray(A) == 1)
    A = [0,2,1,0]
    print(solution.peakIndexInMountainArray(A) == 1)
