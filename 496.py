class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def find_greater(num):
            for i in range(nums.index(num), len(nums)):
                if nums[i] > num:
                    return nums[i]
            else:
                return -1
        return [find_greater(item) for item in findNums]

        d = {}
        s = []
        for i, num in enumerate(nums):
            d[num] = -1
            while len(s) > 0 and num > s[-1]:
                d[s[-1]] = num
                s.pop()
            s.append(num)
        return [d[num] for num in findNums]
