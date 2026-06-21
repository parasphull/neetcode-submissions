class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        grids = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].append(board[i][j])
                    cols[j].append(board[i][j])
                    grids[(i//3)*3+(j//3)].append(board[i][j])
        
        for i in range(9):
            row_set= set(rows[i])
            col_set= set(cols[i])
            grid_set = set(grids[i])

            if len(row_set) != len(rows[i]) or len(col_set) != len(cols[i]) or len(grid_set) != len(grids[i]):
                return False
        
        return True