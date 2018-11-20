class Solution(object):
    def countAndSay(self, n):
        """

        :param n: int
        :return: int
        """

        res = '1'
        for i in range(n - 1):
            res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
        return res


import itertools
S1 = Solution()
print(S1.countAndSay(2))

