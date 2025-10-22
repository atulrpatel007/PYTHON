from collections import Counter


class Solution(object):
    def majorityElement(self, n):
        d = Counter(n)
        r = []
        for key in d:
            if d[key] > len(n) // 3:
                r.append(key)
        return r
