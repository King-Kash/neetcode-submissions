class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        last_letter = word[-1]
        row = 0
        col = 0
        final_res = False
        
        def helper(board, word, visited, r, c):
            # base condition
            if len(word) == 0:
                return True

            last_letter = word[-1]
            current_letter = board[r][c]

            # check that the last letter is correct
            position_match = ((last_letter) == (current_letter))
            print(position_match)
            visited.append((r,c))

            # check the surroundings
            res = False
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if ((nr, nc) in visited) or (nr < 0 or nr >= ROWS) or (nc < 0 or nc >= COLS):
                    continue
                
                res = res or (helper(board, word[:-1], visited, nr, nc))
            '''
                Every single recursive call is looking at, adding to, and checking the same exact visited list because for arrays python actually passes
                by refrence not by value. if you wanted to pass a copy you would have had to have done visited + [(r,c)] as the param.

                The "Ghost" Effect: If your algorithm goes down a dead end (e.g., it finds "A-B-C" but needs "A-B-D"), it will leave "C" 
                in that shared list. When it backs up to try a different direction for "D," it sees "C" is already there and thinks that 
                cell is blocked, even though it's actually free to use now.
            '''
            visited.remove((r,c))
            return (position_match and res)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == last_letter:
                    row = r
                    col = c
                    # Make sure to try every possible starting point on the graph
                    final_res = (final_res or helper(board, word, [], row, col))
        return final_res


                




'''
1. We are tasked with finding weather or not the board contains the word, two adjacent letters can only be horizontal or vertical to neighboring cells.

2. How to make the problem strictly smaller
- Make the word we are trying to match a little smaller by cutting off the first or last letter from the word and reducing the search

3. f(board, word, visited) - returns true if the last letter in the word is present at this recursive call and if one of the recurssive calls to the four directions
                    returns true

4. Base cases - word is empty so return True

5. legal ways to make the problem smaller. 
f(board, word-1, visited+1)

6. if (current letter and the current letter not in visited) and (left or right or up or down is True).
'''
        
        

         