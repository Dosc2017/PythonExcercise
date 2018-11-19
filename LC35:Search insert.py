class Solution(object):
    def SearchInsertPos(self, nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            print("left:", left,
                  "mid:", mid,
                  "right:", right)
        return left


nums = [1, 3, 5, 6]
target = 4
S1 = Solution()
print(S1.SearchInsertPos(nums, target))

