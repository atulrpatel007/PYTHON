class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        try:
            float(s)
            return s.lower() not in ["inf", "+inf", "-inf", "nan", "Infinity", "+Infinity", "+infinity", "-infinity",
                                     "-Infinity", "NaN", "infinity"]
        except:
            return False

