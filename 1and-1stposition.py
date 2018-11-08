class Solution(object):
    def RemoveDuplicates(self, nums):
        """
        leetcode 26:
        :param nums:int list
        :return:length of nums without duplicates, int
"""
        index = 0
        for num in nums:

            if index < 1 or num != nums[index - 1]:
                nums[index] = num
                index += 1

        return index, nums

    def RD2(self, nums):
        """
        leetcode 80
        """
        index = 0
        for num in nums:
            if index < 2 or num > nums[index - 2]:
                nums[index] = num
                index += 1
        return index, nums

        return nums


Dup = Solution()
s = [0,0,1,1,1,1,2,3,3]
s1 = [0,0,1,1,1,1,2,3,3]
# 对s进行操作会改变s
# print("操作前：s = s1:",s == s1)
dup1 = Dup.RemoveDuplicates(s)
# print("操作后：s = s1:",s == s1)
# s已经改变
dup2 = Dup.RD2(s1)
print(dup1, '\n', dup2)




