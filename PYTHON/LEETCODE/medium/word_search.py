'''Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.'''

def exist(board: list, word:str):
    ROWS , COLS = len(board), len(board[0])
    path = set()  # we store here the coordenates for not repeat it
    
    def dfs(r, c, i):
        if i == len(word):
            return True  # when we go to the final of the word
        
        if (r < 0 or c < 0 or
            len(word) > ROWS*COLS or
            r >= ROWS or c >= COLS or
            word[i] != board[r][c] or 
            (r,c) in path):
            return False

        # store en the set the (r,c) 
        path.add((r, c))
        
        # check if up , down left, right direction is equal to target
        res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

        # remove after the check
        path.remove((r, c))
        
        return res
    

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
            
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ESEE"

print(exist(board, word))