class Solution(object):
    def searchRange(self, n, t):
        if not n:
            return [-1, -1]

        first, last = -1, -1

        for i in range(len(n)):
            if n[i] == t:
                if first == -1:
                    first = i
                last = i

        return [first, last]
