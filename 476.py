class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(str(1 - int(n)) for n in bin(num)[2:]), 2)


if __name__ == '__main__':
    print(Solution().findComplement(5) == 2)
