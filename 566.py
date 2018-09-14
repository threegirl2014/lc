class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        temp = []
        for item in nums:
            temp.extend(item)
        result = []
        for i in range(0, len(temp), c):
            result.append(temp[i: i + c])
        return result
