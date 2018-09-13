class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin_n = bin(N)[2:]
        gap = 0
        first = -1
        for index, item in enumerate(bin_n):
            if item == '1':
                if first == -1:
                    first = index
                else:
                    gap = max(gap, index - first)
                    first = index
        return gap
