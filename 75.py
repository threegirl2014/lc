class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
#        nums.sort()
        zero = 0
        two = len(nums) - 1

        for i in range(len(nums)):
            while i < two and nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            while i > zero and nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
