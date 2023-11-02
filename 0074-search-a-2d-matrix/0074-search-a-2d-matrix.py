class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in matrix:
            l = 0
            r = cols - 1
            while l <= r:
                m = (l+r)//2
                if target < row[m]:
                    r = m - 1
                elif target > row[m]:
                    l = m + 1
                else:
                    return True
        return False
