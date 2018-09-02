class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        exception_index = []
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                exception_index.append(i)
            if len(exception_index) >= 2:
                return False
        exception_index_length = len(exception_index)
        if exception_index_length == 0:
            return True
        else:
            index = exception_index[0]
            if index == 0 or index == n - 2 or nums[index - 1] <= nums[index + 1] or nums[index] <= nums[index + 2]:
                return True
            else:
                return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPossibility([4,2,3]))
    print(solution.checkPossibility([4,2,1]))
