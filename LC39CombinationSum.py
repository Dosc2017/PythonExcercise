class Solution(object):
    """
    def CombinationSum(self, nums, target):

        my version
        :param nums: List[int]
        :param target: int
        :return: List[List[int]]
        may be wrong version


        res = []

        def seeking(sums, index, comb):
            if sums > target:
                return
            if sums == target and comb not in res:
                res.append(comb)
            if index > len(nums) - 1:
                return
            print(sums, index, comb, '\n')
            seeking(sums, index+1, comb)
            seeking(sums+nums[index], index, comb+[nums[index]])

        seeking(0, 0, [])
        return res
         """

    def combinationSum1(self, candidates, target):
        """
        github version
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def helper(remain, combi, idx):
            if remain < 0:
                return
            if remain == 0:
                res.append(combi)
                return
            if idx >= len(candidates):
                return
            print("remain:", remain, "cobmbi:", combi, "index:", idx, "Result:", res)
            helper(remain, combi, idx + 1)
            helper(remain - candidates[idx], combi + [candidates[idx]], idx)

        res = []
        helper(target, [], 0)
        return res


S1 = Solution()
candi = [2, 3, 5]
target = 8
print(S1.CombinationSum(candi, target))
