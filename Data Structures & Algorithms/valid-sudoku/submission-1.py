class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in range(len(board)):
            row_set = set()
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                if board[row][col] in row_set:
                    return False
                else:
                    row_set.add(board[row][col])

        # Check cols
        for col in range(len(board[0])):
            col_set = set()
            for row in range(len(board)):
                if board[row][col] == '.':
                    continue
                if board[row][col] in col_set:
                    return False
                else:
                    col_set.add(board[row][col])

        # Check squares
        for square in range(9):
            square_set = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in square_set:
                        return False
                    else:
                        square_set.add(board[row][col])
        return True

            