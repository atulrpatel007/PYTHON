class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = haystack
        b = needle

        if b in a:
            for i in range(len(a)):
             c = a[i:i+len(b)]
             if a[i] == b[0] and c == b:
                 return i
                 break
        else:
            return -1