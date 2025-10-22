class Solution(object):
    def firstMissingPositive(self, nums):
        nums_set = set(nums)
        target = 1
        while True:
            if target not in nums_set:
                return target
            target += 1