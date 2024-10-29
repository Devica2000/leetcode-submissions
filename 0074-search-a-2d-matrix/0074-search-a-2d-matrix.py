class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False

        row = (top + bot)//2
        l = 0
        r = COLS - 1
        while l<= r:
            m = (l + r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False










        # Time Complexity = O(log(m * n))

        #getting the dimensions of the matrix
        ROWS = len(matrix)
        COLS = len(matrix[0])

        #defining pointers for the row
        top = 0
        bot = ROWS - 1
        while top <= bot:
            mid_row = (top + bot)//2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                #important to break here
                #else the loop will continue to run through all iterations
                #even after finding the correct row
                break

        #means that the element does not satisfy any condition
        #this means it is not present in any of the rows
        if not (top <= bot):
            return False
        
        #applying binary search to the current row
        row = (top + bot)//2
        l,r = 0, COLS - 1
        while l<=r:
            m = (l+r)//2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False

        #brute force - O(m * log n)

        # rows = len(matrix)
        # cols = len(matrix[0])
        # for row in matrix:
        #     l = 0
        #     r = cols - 1
        #     while l <= r:
        #         m = (l+r)//2
        #         if target < row[m]:
        #             r = m - 1
        #         elif target > row[m]:
        #             l = m + 1
        #         else:
        #             return True
        # return False
