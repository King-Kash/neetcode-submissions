class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for row in range(n//2):
            for col in range((n+1)//2):
                val_at_target = 0
                current_val = matrix[row][col]
                c_r = row
                c_c = col
                while True:
                    n_r = c_c 
                    n_c = len(matrix)-1-c_r
                    val_at_target = matrix[n_r][n_c]
                    matrix[n_r][n_c] = current_val
                    current_val = val_at_target
                    if n_r == row and n_c == col:
                        break
                    c_r = n_r
                    c_c = n_c







            
                
        