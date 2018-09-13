from collections import defaultdict


class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d = defaultdict(int)
        for item in A:
            d[self.swap_str(item)] += 1
        return len(d)

    def swap_str(self, s):
        s_odd = s[::2]
        s_even = s[1::2]
        return ''.join(sorted(s_odd)) + ''.join(sorted(s_even))
