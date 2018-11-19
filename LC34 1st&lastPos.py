class Solution(object):
    def FindPos(self, nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return: List[int]

        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if left < len(nums):
            if nums[left] != target:
                return [-1, -1]
        else:
            return [-1, -1]
        right = left

        if right == len(nums) - 1:
            return [left, right]

        while right <= len(nums) -1:
            if nums[right] == target:
                right += 1
            else:
                break

        return [left, right - 1]


S1 = Solution()
s = [2, 2]
tar = 2
print(S1.FindPos(s, tar))
