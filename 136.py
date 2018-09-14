class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i += 2
        return nums[-1]

        s = set()
        for item in nums:
            if item in s:
                s.remove(item)
            else:
                s.add(item)
        return s.pop()

        result = 0
        for item in nums:
            result ^= item
        return result
