from collections import Counter


class Solution(object):
    def canConstruct(self, r, m):
        """
        :type r: str  (ransomNote)
        :type m: str  (magazine)
        :rtype: bool
        """
        d = Counter(r)
        f = Counter(m)

        for key in d:
            if d[key] > f[key]:
                return False
        return True