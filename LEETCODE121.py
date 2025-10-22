class Solution(object):
    def maxProfit(self, prices):
        mip, p = float('inf'), 0
        for x in prices:
            if x < mip:
                mip = x
            elif x - mip > p:
                p = x - mip
        return p