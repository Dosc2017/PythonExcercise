class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return

        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                """
                use while not if
                
                """
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                print(i, nums[i])

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


S1 = Solution()
nums = [-1,4,2,1,9,10]
print(S1.firstMissingPositive(nums))


