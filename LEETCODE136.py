from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        d = Counter(nums)
        for key in d:
            if d[key] == 1:
                return key