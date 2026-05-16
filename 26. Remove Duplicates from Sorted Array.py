class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = sorted(set(nums))

        for i in range(len(num)):
            nums[i] = num[i]
        return len(num)