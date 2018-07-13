class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
#        x_bin = bin(x)[2:]
#        y_bin = bin(y)[2:]
#        x_bin_len, y_bin_len = len(x_bin), len(y_bin)
#        max_len = max(x_bin_len, y_bin_len)
#        x_bin = '0' * (max_len - x_bin_len) + x_bin
#        y_bin = '0' * (max_len - y_bin_len) + y_bin

#        count = 0
#        for item1, item2 in zip(x_bin, y_bin):
#            if item1 != item2:
#                count += 1
#        return count

#        haming = (int(bool(item1 != item2)) for item1, item2 in zip(x_bin, y_bin))
#        return sum(haming)

        # &按位与; |按位或; ^按位异或; ~取反
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    solution = Solution()
    x, y = 1, 4
    print(2 == solution.hammingDistance(x, y))
