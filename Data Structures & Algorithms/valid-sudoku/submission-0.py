class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not (self.isValidLine(board, i) and self.isValidVert(board, i) and self.isValidSquare(board, i)):
                return False
        return True
        
    def isValidLine(self, board: List[List[str]], idx: int) -> bool:
        s = set()
        for num in board[idx]:
            if num == '.':
                continue
            if num in s:
                return False
            s.add(num)
        return True

    def isValidVert(self, board: List[List[str]], idx: int) -> bool:
        s = set()
        for i in range(9):
            num = board[i][idx]
            if num == '.':
                continue
            if num in s:
                return False
            s.add(num)
        return True

    def isValidSquare(self, board: List[List[str]], idx: int) -> bool:
        row = 3*(int)(idx/3)
        col = 3*(idx%3)
        s = set()
        for i in range(row, row+3):
            for j in range(col, col+3):
                num = board[i][j]
                if num == '.':
                    continue
                if num in s:
                    return False
                s.add(num)
        
        return True
