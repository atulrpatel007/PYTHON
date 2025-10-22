class Solution(object):
    def addBinary(self, a, b):
        r = bin(int(a, 2) + int(b, 2))
        return r[2:]


