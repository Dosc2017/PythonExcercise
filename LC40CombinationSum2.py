class Solution(object):
    def CombinationSum2(self, candidates, target):
        """

        :param candidates: List[int]
        :param target: int
        :return: List[List[int]]
        """
        res = []

        def seeking(remain, index, comb):
            """

            :param remain: int
            :param index: int
            :param comb: List[int]
            :return:
            """
            if remain < 0:
                return
            if remain == 0 and comb not in res:
                res.append(comb)
                return
            if index >= len(candidates):
                return
            seeking(remain, index + 1, comb)
            seeking(remain - candidates[index], index + 1, comb + candidates[index])

        seeking(target, 0, [])
        return res








