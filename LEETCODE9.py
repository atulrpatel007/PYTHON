class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=str(x)
        r=a[::-1]
        return a==r