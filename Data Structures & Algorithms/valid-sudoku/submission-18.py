class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = []
        j = 0
        for row in board:  
            for position in row:
                if position == '.':
                    pass
                elif position in numbers:
                    return False
                else:
                    numbers.append(position)
            numbers.clear()
        for i in range(len(board)):
            for row in board:
                if row[i] == '.':
                    pass
                elif row[i] in numbers:
                    return False
                else:
                    numbers.append(row[i])
            numbers.clear()
        for k in range(0, 9, 3):
            while j < 3:
                for i in range(k, 3 + k):
                    if board[j][i] == '.':
                        pass
                    elif board[j][i] in numbers:
                        return False
                    else:
                        numbers.append(board[j][i])
                j += 1
            numbers.clear()
        return True