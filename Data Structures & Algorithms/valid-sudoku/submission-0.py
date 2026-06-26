def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def check(a):
    arr = remove_values_from_list(a, '.')
    if len(set(arr)) != len(arr):
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            if check(i):
                return False
        for i in list(zip(*board)):
            if check(i):
                return False
        for i in range(3):
            for j in range(3):
                arr = []
                for row in range(i * 3, i * 3 + 3):
                    for col in range(j * 3, j * 3 + 3):
                        arr.append(board[row][col])
                if check(arr):
                    return False
        return True