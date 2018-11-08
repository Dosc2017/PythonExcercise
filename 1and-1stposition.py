class Solution(object):
    def RemoveDuplicates(self, nums):
        index = 0
        for num in nums:

            if index < 1 or num != nums[index - 1]:
                nums[index] = num
                index += 1


        return index, nums[:index]


Dup = Solution()
s = [1, 2, 2, 2, 4, 5, 5]
dup1 = Dup.RemoveDuplicates(s)
print(dup1)


