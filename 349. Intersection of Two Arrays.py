class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

        # result = []

        # for i in nums1:
        #     for j in nums2:
        #         if i == j:
        #             result.append(i)
        #             result = list(set(result))
        # return result