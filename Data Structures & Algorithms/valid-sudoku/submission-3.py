class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == ".":
                    continue
                current_square = (row // 3, col // 3)
                if (val in rows[row] or val in cols[col] or val in squares[current_square]):
                    return False
                rows[row].add(val)
                cols[col].add(val)
                squares[current_square].add(val)
        return True