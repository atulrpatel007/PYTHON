class Solution(object):
    def searchMatrix(self, matrix, target):
        if any(target in row for row in matrix):
            return True
        else:
            return False
