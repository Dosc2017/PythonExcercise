class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        can only trap water with one highest
        """
        res, highest = 0, max(height)




s1 = Solution()
s = [0,1,0,2,1,0,1,3,2,1,2,1]

print(s1.trap(s))



