class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        return int(dividend / float(divisor))  