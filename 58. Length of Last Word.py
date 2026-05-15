class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        
        lst_word = s[-1]
        length = len(lst_word)
        return length