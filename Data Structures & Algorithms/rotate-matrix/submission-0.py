class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                val = (matrix[row][col] % 100) * 100
                n_r = col
                n_c = len(matrix)-1-row
                matrix[n_r][n_c] += val
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = int(matrix[row][col]/100)
        
        print(matrix)

            
                
        