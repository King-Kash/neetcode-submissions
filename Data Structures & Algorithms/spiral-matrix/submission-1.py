class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #intilize
        row_top = 0 
        col_start = 0 
        row_bottom = len(matrix)-1
        col_end = len(matrix[0])-1
        row_limit = 0
        col_limit = 0

        #define the bounds:
        # rows
        if len(matrix) % 2 == 1:
            row_limit = len(matrix) // 2 + 1
        else:
            row_limit = len(matrix) // 2
        # col
        if len(matrix[0]) % 2 == 1:
            col_limit = len(matrix[0]) // 2 + 1
        else:
            col_limit = len(matrix[0]) // 2
 
        res = []

        print("Row Limit: ", row_limit, "Col Limit: ", col_limit)


        while True:
            # PRINT CONCENTRIC RINGS OUTERMOST TO INNERMOST
            print("Top Row: ", row_top, "Start Col: ", col_start)
            # top
            for c in range(col_start, col_end + 1):
                res.append(matrix[row_top][c])
            # right
            for r in range(row_top + 1, row_bottom + 1):
                res.append(matrix[r][col_end])

            if (col_start != col_end) and (row_top != row_bottom):    
                # bottom
                for c in range(col_end - 1, col_start - 1, -1):
                    res.append(matrix[row_bottom][c])
                # left
                for r in range(row_bottom - 1, row_top, -1):
                    res.append(matrix[r][col_start])
            
            print("Ring End")

            if row_top < row_limit:
                row_top += 1
                row_bottom -= 1
            if col_start < col_limit:
                col_start += 1
                col_end -= 1

            if row_top >= row_limit or col_start >= col_limit:
                break
        
        return res


