# LeetCode 289. 

"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
"""

def gameOfLife(self, board: List[List[int]]) -> None:
    
    """
    1 - 1 if nei 2, 3
    1 - 0 else (< 2, > 3)
    
    0 - 1 if nei 3
    0 - 0 else (< 3, > 3)
    """
    
    # original | new | state
    #     0    |  0  |   0
    #     1    |  0  |   1
    #     0    |  1  |   2
    #     1    |  1  |   3
    
    def countNeighbours(r, c):
        nei = 0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if ((i == r and j == c) or i < 0 or j < 0 or i == ROWS or j == COLS):
                    continue
                if board[i][j] in [1, 3]:
                    nei+=1
        return nei
    
    ROWS, COLS = len(board), len(board[0])
    
    for r in range(ROWS):
        for c in range(COLS):
            nei = countNeighbours(r, c)
            if board[r][c]:
                if nei in [2, 3]:
                    board[r][c] = 3
            else:
                if nei == 3:
                    board[r][c] = 2
                
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                board[r][c] = 0
            elif board[r][c] in [2, 3]:
                board[r][c] = 1
								
