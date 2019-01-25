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


def pow1(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1/pow1(x, -n)
    if n & 1:
        return x * pow1(x*x, n >> 1)
    else:
        return pow1(x*x, n >> 1)


print(pow1(2, 10), pow(2, 10))


# Leetcode 53: max sub array problem, Kadane algorithm
def maxSubArray(nums):
    max_sum, max_end = nums[0], nums[0]
    for i in range(len(nums)):
        max_end = max(max_end + nums[i], nums[i])
        max_sum = max(max_sum, max_end)
        print('max_end:{},     max_sum:{}'.format(max_end, max_sum))
    return max_sum


input = [-2,-1,-3,-4,-1,-2,-1,-5,-4]

s = 'wa'


def merge_interval(intervals):
    """
    Leetcode 56: Merge intervals
    :param intervals: List[int]
    :return:
    """
    res = []
    for i in sorted(intervals, key= lambda x: x[0]):
        if res and res[-1][-1] >= i[0]:
            res[-1][-1] = max(i[-1], res[-1][-1])
        else:
            res.append(i)

    return res


