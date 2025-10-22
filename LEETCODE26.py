class Solution(object):
    def removeDuplicates(self, n):
        un = sorted(set(n))
        k = len(un)
        for i in range(k):
            n[i] = un[i]
        return k




