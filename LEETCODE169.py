class Solution(object):
    def majorityElement(self, n):
        count = 0
        candidate = None

        for num in n:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate