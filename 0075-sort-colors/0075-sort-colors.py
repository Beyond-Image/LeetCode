class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for x in range(len(nums)):
            for y in range(x):
                if(nums[x] < nums[y]):
                    temp = nums[x]
                    nums[x] = nums[y]
                    nums[y] = temp
        