class Solution:
    def solve(self, board: List[List[str]]) -> None:
        roots = []
        # Phase 1 - Find all the 0's
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    roots.append((r,c))
        
        

        # Phase 2 - DFS to group regions of 'O's, check if any of them touch a boundary, if they dont turn them all into X
        def dfs(root):
            if not root:
                return
            
            stack = []
            stack.append(root)
            Explored = defaultdict(bool)

            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            corner_piece = False
            pieces = []

            while stack:
                current = stack.pop()
                if Explored[current] == False:
                    Explored[current] = True
                    pieces.append(current)
                    c_r = current[0]
                    c_c = current[1]
                    if c_r == 0 or c_r == len(board)-1 or c_c == 0 or c_c == len(board[0])-1:
                        if board[c_r][c_c] == "O":
                            corner_piece = True
                            break
                    for direction in directions:
                        n_r = current[0] + direction[0]
                        n_c = current[1] + direction[1]
                        if n_r >= 0 and n_r < len(board) and n_c >= 0 and n_c < len(board[0]) and board[n_r][n_c] == "O":
                                stack.append((n_r, n_c))
                        

            if corner_piece:
                return
            else:
                for piece in pieces:
                    r = piece[0]
                    c = piece[1]
                    board[r][c] = "X"
        
        for root in roots:
            dfs(root)
        