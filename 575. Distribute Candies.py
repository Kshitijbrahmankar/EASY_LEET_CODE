class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        return min(len(set(candyType)), len(candyType) // 2)

        # FAILED AT THE 189TH TESTCASE ||
        #                              \/
        # n = len(candyType) 
        # candy = set(candyType)
        # count = 0
        # for i in candyType:
        #     if len(candy) == 1:
        #         n = n // n
        #         return n
        #     else:
        #         n = n // 2
        #         return n 