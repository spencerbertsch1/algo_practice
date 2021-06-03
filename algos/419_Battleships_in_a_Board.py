class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        counter: int = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j])
                if board[i][j] == "X":
                    if (i>0) and (board[i-1][j] == "X"):
                        print('skipping - X found above')
                    elif (j>0) and (board[i][j-1] == "X"):
                        print('skipping - X found left')
                    else:
                        # only increment the counter if we hit the upper left part of a battleship
                        counter+=1
                        print('hit')
                    
        return counter
