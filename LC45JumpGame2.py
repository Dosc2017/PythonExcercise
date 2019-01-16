class Solution:
    def jump(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        current_end, current_farthest, steps = 0, 0, 0
        for i in range(len(nums)-1):
            current_farthest = max(current_farthest, i + nums[i])
            if current_farthest >= len(nums) - 1:
                steps += 1

                return steps
            if i == current_end:
                current_end = current_farthest
                steps += 1



        return steps


s = Solution()
step = [2, 5, 2, 1, 1, 1, 1, 4]
print(s.jump(step))



# Leetcode 46: permutation
from itertools import permutations
print(list(permutations([1, 2, 3])))


# Leetcode 47: rotate matrix
x = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
x[:] = zip(*x[::-1])
print(x)