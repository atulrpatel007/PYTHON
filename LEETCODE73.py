class Solution(object):
    def setZeroes(self, m):
        R, C = len(m), len(m[0])
        rows, cols = set(), set()
        for i in range(R):
            for j in range(C):
                if m[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    m[i][j] = 0
        return m

