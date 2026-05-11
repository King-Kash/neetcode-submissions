class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        while (row <= len(matrix)-1) and (col >= 0):
            print(matrix[row][col])
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                col -= 1
                if col >= 0:
                    if target > matrix[row][col]:
                        return False
            else:
                row += 1
        return False
