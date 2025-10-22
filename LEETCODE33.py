class Solution(object):
    def search(self, n, t):
        if t in n:
            return n.index(t)
        else:
            return -1

