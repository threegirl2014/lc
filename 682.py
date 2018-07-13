class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        round_points = []
        for op in ops:
            if op == 'C':
                round_points.pop()
            elif op == 'D':
                round_points.append(2 * round_points[-1])
            elif op == '+':
                round_points.append(sum(round_points[-2:]))
            else:
                round_points.append(int(op))
        return sum(round_points)
