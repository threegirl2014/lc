
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for item in S:
            if item in J:
                count += 1

        return count


class Solution2:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for item in J:
            count += S.count(item)

        return count


if __name__ == '__main__':
    solution = Solution2()
    J = "aA"
    S = "aAAbbbb"
    print(3 == solution.numJewelsInStones(J, S))
    J = "z"
    S = "ZZ"
    print(0 == solution.numJewelsInStones(J, S))
