
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        import math
        message_mount = minutesToTest / minutesToDie + 1
        pigs_mount = math.log(buckets, message_mount)

        return int(math.ceil(pigs_mount))


Peggy = Solution()
a = Peggy.poorPigs(1000, 15, 60)
print(a)


